BIN = main
OBJECTS = main.o

all : $(BIN)

$(BIN): $(OBJECTS)
	$(CXX) -o $@ $(OBJECTS) $(WARN_FLAGS)

%.o: %.cpp optparse.h
	$(CXX) $(WARN_FLAGS) -c $< -o $@

check: main.o
	$(CXX) -o tmp_test test.o tmp_second.cc
	rm tmp_second.cc
	./tmp_test
	rm tmp_test

clean:
	rm -f *.o $(BIN)


.PHONY: check clean
