SRC = ./src
APPS = ./apps
BIN = ./bin
OBJ = ./obj
INCLUDE = ./include

all: libed myapps

libed: \
	float_vector.o \
	mytime.o

myapps:
	gcc $(APPS)/app.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_mytime.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_mytime

%.o: $(SRC)/%.c $(INCLUDE)/%.h
	gcc -c $< -I $(INCLUDE) -o $(OBJ)/$@

run:
	$(BIN)/app

clean:
	rm -rf $(BIN)/* $(OBJ)/*
