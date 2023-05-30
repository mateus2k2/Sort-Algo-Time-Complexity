#make -s --> Suppresses other makefile messages

all: driver.o insertionSort.o mergeSort.o radixSort.o 
	@gcc ./src/obj/driver.o ./src/obj/insertionSort.o ./src/obj/mergeSort.o ./src/obj/radixSort.o -o ./bin/runner.exe -Wall

degub: 
	@gcc ./src/*.c -o ./bin/degub.exe -g

degubRun:
	@gdb ./bin/degub.exe

# ------------------------------------------------------------------------------

driver.o: ./src/driver.c
	@gcc -c ./src/driver.c -o ./src/obj/driver.o -Wall

insertionSort.o: ./src/insertionSort.c
	@gcc -c ./src/insertionSort.c -o ./src/obj/insertionSort.o -Wall

mergeSort.o: ./src/mergeSort.c
	@gcc -c ./src/mergeSort.c -o ./src/obj/mergeSort.o -Wall

radixSort.o: ./src/radixSort.c
	@gcc -c ./src/radixSort.c -o ./src/obj/radixSort.o -Wall

# ------------------------------------------------------------------------------

run:
	@./bin/runner.exe $(SIZE) >> ./output/output.csv

# teste:
# 	@./scripts/runTests.sh
# ------------------------------------------------------------------------------

go:
	@make -s clean
	@make -s all
	@make -s run

# ------------------------------------------------------------------------------

clean:
	# @cd ./bin && rm ./*.exe 
	# @cd ./src/obj && rm ./*.o
	# @clear
