import random

replacers = ["tappade kjolen", "hittade en anka", "stefan", "bygg hasse", "superwoman"]

rand = random.randint(0, 4)
rand1 = random.randint(0, 4)
rand2= random.randint(0, 4)
rand3 = random.randint(0, 4)

print(f"""En app {replacers[rand]} kan laddas ned till mobiltelefonen ska varna

finländare som kommit nära {replacers[rand1]} som smittats med coronaviruset.

– Jag tycker att ni i Sverige borde överväga att göra något

liknande, säger Markku Tervahauta, {replacers[rand2]} för

Finska {replacers[rand3]} för hälsa och välfärd, THL.""")
