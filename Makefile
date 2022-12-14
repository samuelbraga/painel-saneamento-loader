verify:
	flake8 app/
	bandit app/

run:
	./bin/migrate_data.sh