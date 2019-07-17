#include <iostream>
#include <string>
#include <fstream>


int main(int argc, char** argv) {
    std::string filePath;

    if(argc != 2) {
        std::cout << "Usage: ./lint path/to/file" << std::endl;
        return 1;
    }

    filePath = argv[1];

    std::cout << "Displaying contents of: " << filePath << std::endl;

    readAndDisplayFile(filePath);
    return 0;
}

/*
    Reads and displays file with name `filename`.
*/
void readAndDisplayFile(std::string filename) {
    std::fstream myFile(filename.c_str());

    if (!myFile.is_open()) {
        std::cout << "Could not open file." << std::endl;
        return;
    }

    std::string currentLine;
    while ((std::getline (myFile, currentLine))) {
        std::cout << currentLine;
    } 

    myFile.close();
}
