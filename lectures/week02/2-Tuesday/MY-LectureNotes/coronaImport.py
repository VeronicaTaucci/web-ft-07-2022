import corona

corona_data = corona.data

total_recovered = 0
most_recovered = 0
least_recovered = 0
for idx in corona_data:
    total_recovered += idx['recovered']
    if idx['recovered'] > most_recovered:
        most_recovered = idx['recovered']
        most_recovered_state = idx['state']
    if idx['recovered'] < most_recovered:
        least_recovered = idx['recovered']
        least_recovered_state = idx['state']
    print(f"""\tState : {idx['state']}
        Recovered : {idx['recovered']}
        Active cases : {idx['active']}\n""")
print(f"""\n\t Total Recovered : {total_recovered}
    Most recovered : {most_recovered_state} : {most_recovered}
    Least recovered : {least_recovered_state} : {least_recovered}""")
