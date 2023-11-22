program P120
    implicit none
    integer :: N, result, i
    double precision :: start, finish

    N = 1000
    call cpu_time(start)
    result = 0

    do i = 3, N
        result = result + maxRemainder(i)
    end do

    call cpu_time(finish)
    print *, 'Result of P120: ', result
    print *, 'Execution time: ', finish - start, ' seconds'

contains

    ! Calculate the maximum remainder for a given 'a'
    function maxRemainder(a) result(maxR)
        integer, intent(in) :: a
        integer :: maxR, n, r, remainders(a*a), count, j
        logical :: found

        maxR = 0
        n = 1
        count = 0

        do while (.TRUE.)
            r = mod((a - 1)**n + (a + 1)**n, a**2)

            ! Check if the remainder is already found
            found = .FALSE.
            do j = 1, count
                if (remainders(j) == r) then
                    found = .TRUE.
                    exit
                end if
            end do

            if (found) exit

            count = count + 1
            remainders(count) = r
            maxR = max(maxR, r)

            n = n + 2  ! Increment by 2 as even 'n' does not produce max remainder
        end do
    end function maxRemainder

end program P120
