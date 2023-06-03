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

testes:
	@bash ./scripts/runTests.sh
	@make -s t

avr:
	@cd ./statistic && python3 average.py && cd ./.. 

bar:
	@cd ./statistic && python3 barGraphs.py && cd ./..

gra:
<<<<<<< HEAD
	@cd ./statistic && python3 graphs.py && cd ./..
=======
	@cd ./statistic && python graphs.py && cd ./..

conf:
	@cd ./statistic && python ConfidenceGraph.py && cd ./..

t:
	@cd ./statistic && python3 tTeste.py && cd ./..
>>>>>>> f11d368c876beac2aa908020587f4a8354c230b3

t:	
	@cd ./output && rm ./*.out && cd ./..
	@cd ./statistic && python3 tTeste.py >> ../output/resultados.out && cd ./..
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
