! This program is designed to generate sequences from a seed value.
program Main
    implicit none
    real(8) :: seed
    character(len=50) :: number

    ! Initialize the seed value.
    seed = 2.2_8

    ! This loop iteratively generates sequences from the seed and updates the seed
    ! if the sequence is larger than the current seed.
    do
        number = genSequence(seed, 24)
        if (dble(number) > seed) then
            seed = dble(number)
        else
            exit
        end if
    end do

    ! Print the resulting sequence.
    print *, "Result: ", number

contains

    ! The genNext function is designed to produce the next term in a sequence based on a given value.
    ! This function computes the next term using a formula that involves the floor operation and arithmetic operations.
    ! Time Complexity: O(1) [Constant time]
    ! Space Complexity: O(1) [Constant space]
    real(8) function genNext(bn)
        implicit none
        real(8), intent(in) :: bn
        genNext = floor(bn) * (bn - floor(bn) + 1.0_8)
    end function genNext

    ! The genSequence function is responsible for generating a sequence of terms up to a specified number of decimals.
    ! The sequence is generated iteratively by continuously computing the next term until the desired precision is achieved.
    ! Time Complexity: O(n) [Where n is the desired length/precision]
    ! Space Complexity: O(n) [Storage for the number string]
    character(len=50) function genSequence(seed, decimals)
        implicit none
        real(8), intent(in) :: seed
        integer, intent(in) :: decimals
        character(len=10) :: term
        integer :: i

        ! Convert the seed value to its integer representation and initialize the sequence string with it.
        write(genSequence, '(F0.0)') seed
        genSequence = genSequence // '.'

        ! This loop is used to continuously generate terms in the sequence until the desired length is achieved.
        do i = 1, decimals
            seed = genNext(seed)
            write(term, '(F0.0)') seed
            genSequence = genSequence // trim(term)
        end do
    end function genSequence

end program Main
