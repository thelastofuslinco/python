n = int(input('Digite um numero? '))

fibonacci = {
    'prev': 0,
    'next': 1,
}
print(fibonacci['prev'])
print(fibonacci['next'])
while n > 2:
    n -= 1
    fibonacci['next'] = fibonacci['prev'] + fibonacci['next']
    print(fibonacci['next'])
    fibonacci['prev'] = fibonacci['next'] - fibonacci['prev']
