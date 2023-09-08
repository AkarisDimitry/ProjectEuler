section .data
    upper_bound db 10000
    threshold dd 10000000000
    sieve db 10001 dup(1) ; array of bytes initialized to 1

section .text
    global _start

_start:
    ; Initialize sieve[0] and sieve[1] to 0
    mov [sieve], byte 0
    mov [sieve + 1], byte 0

    ; Starting the loop to mark non-primes
    mov ecx, 2 ; start with the first prime number

outer_loop:
    ; Check if current number is marked as prime
    mov al, [sieve + ecx]
    test al, al
    jz next_number

    ; Mark multiples of the current number as non-prime
    mov edx, ecx
mark_multiples:
    add edx, ecx
    cmp edx, upper_bound
    ja next_number
    mov [sieve + edx], byte 0
    jmp mark_multiples

next_number:
    inc ecx
    cmp ecx, upper_bound
    jbe outer_loop

    ; Now search for the result
    mov ecx, 2
search_result:
    ; Check if current number is prime
    mov al, [sieve + ecx]
    test al, al
    jz next_prime

    ; Calculate 2 + 2 * current number
    add eax, 2
    shl eax, 1 ; multiply by 2
    cmp eax, threshold
    jg found_result

next_prime:
    inc ecx
    cmp ecx, upper_bound
    jbe search_result

found_result:
    ; At this point, ECX contains the result
    ; You can print or store it as needed

    ; Exit the program (for simplicity, using an interrupt, but this will vary by OS)
    int 0x80
