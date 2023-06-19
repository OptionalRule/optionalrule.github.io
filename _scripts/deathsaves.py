import random

def roll_die():
    return random.randint(1, 20)

def perform_death_save(outcomes):
    successes = 0
    failures = 0

    attempts = 0
    while successes < 3 and failures < 3:
        attempts += 1
        roll = roll_die()
        if roll == 20:
            successes = 3
            outcomes['weakup'] += 1
        elif roll >= 10:
            successes += 1
        elif roll == 1:
            failures += 2
        else:
            failures += 1

    if successes == 3:
        outcomes['successes'] += 1
        outcomes['rolls_to_succeed'] += attempts
    else:
        outcomes['failures'] += 1
        outcomes['rolls_to_fail'] += attempts

def simulate_death_saves(num_cases):
    outcomes = {'successes': 0, 'failures': 0, 'weakup': 0, 'rolls_to_fail': 0, 'rolls_to_succeed': 0}

    for _ in range(num_cases):
        perform_death_save(outcomes)

    success_count = outcomes['successes']
    wakeups = outcomes['weakup']
    failure_count = outcomes['failures']
    success_rate = success_count / num_cases * 100
    wakeups_rate = wakeups / num_cases * 100
    failure_rate = failure_count / num_cases * 100

    print(f"Successes: {success_count}")
    print(f"Wakeups: {wakeups}")
    print(f"Failures: {failure_count}")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Wakeup rate: {wakeups_rate:.2f}%")
    print(f"Failure rate: {failure_rate:.2f}%")
    print("---------------------------")
    print(f"Average rolls to succeed: {outcomes['rolls_to_succeed'] / success_count:.2f}")
    print(f"Average rolls to fail: {outcomes['rolls_to_fail'] / failure_count:.2f}")

def main():
    num_cases = 10000000
    simulate_death_saves(num_cases)

if __name__ == "__main__":
    main()
