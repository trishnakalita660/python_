#  without generators

def square_list(nums):
    result = []
    for x in nums:
        result.append(x*x)
    return result

sq_list = square_list([1,2,3,4,5])
print (sq_list)

# using generators

# --> Generators don't hold the entire result(list) in the memory instead
# it yield the result one at a time

#  Generators has better performance in terms of memory management

def generate_list(nums):
    
    for x in nums:
        yield(x*x)
     
gen_list = generate_list([1,2,3,4,5])
print (gen_list) # generator object

for gen in gen_list:
    print(gen)

# using list comprehension

generate = (x*x for x in [1,2,3,4,5]) # () returns it as generator object

generate = list(generate)

print(generate)
