# CustomRandomNumberGenerator
Biased RNG
# =============================================================================
#      customrandom.py module recieves a
#      seed, minimum, and maximum number and generates a random number using
#      the "Next()" function. Each time the "Next()" function is called, a new
#      random number is generated and returned to the caller
# =============================================================================


#     MyRNG class: This is the class declaration for the random number
#     generator. The constructor initializes data members "m_min" and
#     "m_max" which stores the minimum and maximum range of values in which
#     the random numbers will generate. There is another variable named "m_seed"
#     which is initialized using the method Seed(), and stores the value of the
#     current seed within the class. Using the obtained values from above, the
#     "Next()" method returns a random number"


#    This method is based on a	more general version of the PRNG algorithms used in these examples is	
#    called linear congruential	generator.
#    Given the	current	value xi of PRNG using	the linear congruential	generator method, we can compute the next	
#    value in the sequence, xi+1, using	the formula xi+1=(a *xi + c) modulo m where a, c,and m	are predetermined constants.	
#    If	we choose a large value	for m,	and appropriate	 values	for a	and c	that work with	this m,then we	can	
#    generate	a very	long	sequence before	numbers	begin	to repeat.	
#    Ideally,	we could generate a sequence with a maximum period of	m
#    The LCG will have	a period of m for all seed values if and only	if:	
#    c	and m	are relatively	prime	(i.e. the only	positive integer that divides both	c and	m is 1)	
#    a-1 is divisible by all	prime	factors	of m if	m is a	multiple of 4,then a-1	is also	a multiple of	4
