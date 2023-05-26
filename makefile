#make -s --> Suppresses other makefile messages

all: driver.o insertionSort.o mergeSort.o radixSort.o 
	@g++ ./src/obj/driver.o ./src/obj/insertionSort.o ./src/obj/mergeSort.o ./src/obj/radixSort.o -o ./bin/runner.exe -Wall

degub: 
	@g++ ./src/*.c -o ./bin/degub.exe -g

degubRun:
	@gdb ./bin/degub.exe

# ------------------------------------------------------------------------------

driver.o: ./src/driver.c
	@g++ -c ./src/driver.c -o ./src/obj/driver.o -Wall

insertionSort.o: ./src/insertionSort.c
	@g++ -c ./src/insertionSort.c -o ./src/obj/insertionSort.o -Wall

mergeSort.o: ./src/mergeSort.c
	@g++ -c ./src/mergeSort.c -o ./src/obj/mergeSort.o -Wall

radixSort.o: ./src/radixSort.c
	@g++ -c ./src/radixSort.c -o ./src/obj/radixSort.o -Wall

# ------------------------------------------------------------------------------

run:
	@./bin/runner.exe > ./out/output.csv

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
