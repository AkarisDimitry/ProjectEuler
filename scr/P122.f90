program main
    implicit none
    integer :: M, result
    double precision :: start_time, end_time, elapsed_time

    M = 200
    call cpu_time(start_time)
    result = P122(M)
    call cpu_time(end_time)
    elapsed_time = end_time - start_time
    print *, 'Resultado: ', result, ' (execution time ', elapsed_time, ' seconds)'
contains

    recursive function sum_chain(L, L_size, N, suma_actual, lenth_min, length_actual) result(res)
        integer, intent(in) :: L_size, N, suma_actual, length_actual
        integer :: lenth_min
        integer, intent(in) :: L(L_size)
        integer :: res, local_l, suma_actual_l, newL_size, i
        logical :: exists
        integer, allocatable :: newL(:)

        res = lenth_min
        do i = L_size, 1, -1
            local_l = L(i)
            suma_actual_l = suma_actual + local_l

            if (suma_actual_l > N) cycle
            if (suma_actual_l == N .and. length_actual < lenth_min) then
                res = length_actual
                return
            end if
            if (suma_actual_l < N .and. length_actual < lenth_min) then
                exists = any(L == suma_actual_l)
                if (.not. exists) then
                    newL_size = L_size + 1
                else
                    newL_size = L_size
                end if
                allocate(newL(newL_size))
                newL(1:L_size) = L
                if (.not. exists) newL(L_size+1) = suma_actual_l
                res = sum_chain(newL, newL_size, N, suma_actual_l, lenth_min, length_actual+1)
                deallocate(newL)
                if (res < lenth_min) lenth_min = res
            end if
        end do
    end function sum_chain

    function P122(M) result(total)
        integer, intent(in) :: M
        integer :: total, n, L(1)
        L(1) = 1
        total = 0
        do n = 1, M
            total = total + sum_chain(L, 1, n, 0, 9999, 0)
        end do
    end function P122

end program main
