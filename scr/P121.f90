program disc_game
    implicit none
    integer :: n, m, result
    real(8) :: start_time, end_time, elapsed_time

    n = 15
    m = 8

    call cpu_time(start_time)
    result = P121(n, m)
    call cpu_time(end_time)

    elapsed_time = end_time - start_time
    print *, "Resultado de P121: ", result, "(tiempo de ejecución ", elapsed_time, "s)"

contains

    recursive subroutine combine(start, n, k, current, combinations, count)
        integer, intent(in) :: start, n, k
        integer, dimension(:), intent(inout) :: current
        integer, dimension(:,:), intent(inout) :: combinations
        integer, intent(inout) :: count

        integer :: i

        if (k == 0) then
            count = count + 1
            combinations(count, :) = current
            return
        end if

        do i = start, n
            current(k) = i
            call combine(i + 1, n, k - 1, current, combinations, count)
        end do
    end subroutine combine

    function in_array(value, array) result(is_in)
        integer, intent(in) :: value
        integer, dimension(:), intent(in) :: array
        logical :: is_in

        is_in = any(array == value)
    end function in_array

    function P121(n, m) result(res)
        integer, intent(in) :: n, m
        integer :: res
        integer, dimension(n) :: current
        integer, dimension(100000, n) :: combinations
        integer :: i, j, k, count
        real(8) :: prob, p_k

        prob = 0.0d0

        do k = m, n
            count = 0
            call combine(1, n, k, current, combinations, count)

            do i = 1, count
                p_k = 1.0d0
                do j = 1, k
                    p_k = p_k * (1.0d0 / (real(combinations(i, j)) + 1.0d0))
                end do

                do j = 1, n
                    if (.not. in_array(j, combinations(i, 1:k))) then
                        p_k = p_k * (1 - (1.0d0 / (real(j) + 1.0d0)))
                    end if
                end do

                prob = prob + p_k
            end do
        end do

        res = nint(1.0d0 / prob)
    end function P121

end program disc_game


! gfortran -o P121 P121.f90
! 