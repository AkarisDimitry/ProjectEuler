program P205
    implicit none

    integer, parameter :: max_dice_sum = 36
    double precision :: peter_distribution(max_dice_sum)
    double precision :: colin_distribution(max_dice_sum)
    double precision :: peter_beats_colin_probability
    double precision :: start, finish
    integer :: i

    call cpu_time(start)

    call calculate_probability_distribution(9, 4, peter_distribution)
    call calculate_probability_distribution(6, 6, colin_distribution)

    peter_beats_colin_probability = 0.0d0
    do i = 1, max_dice_sum
        peter_beats_colin_probability = peter_beats_colin_probability + &
            peter_distribution(i) * sum(colin_distribution(1:i-1))
    end do

    call cpu_time(finish)
    print *, 'Execution time: ', finish - start, ' seconds'
    print *, 'Probability that Pyramidal Peter beats Cubic Colin: ', peter_beats_colin_probability

end program P205

subroutine calculate_probability_distribution(num_dice, sides, distribution)
    integer, intent(in) :: num_dice, sides
    double precision, intent(out) :: distribution(*)
    integer :: i, j, outcomes, sum, count(sides*num_dice)
    double precision :: total_outcomes

    count = 0
    outcomes = int(sides**num_dice)
    total_outcomes = dble(outcomes)

    do i = 0, outcomes - 1
        sum = 0
        j = i
        do while (j > 0)
            sum = sum + mod(j, sides) + 1
            j = j / sides
        end do
        count(sum) = count(sum) + 1
    end do

    do i = num_dice, sides*num_dice
        distribution(i) = dble(count(i)) / total_outcomes
    end do

end subroutine calculate_probability_distribution
