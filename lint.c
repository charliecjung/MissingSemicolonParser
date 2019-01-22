#include <iostream>
#include <string>
#include <fstream>


int main(int argc, char** argv) {
    std::string filePath = "";
    if (argc > 1) {
        filePath = argv[1];
    } else if(argc == 1) {
       std::cout << "Please enter the following text file you would like to modify: ";
       std::cin >> filePath; 

    }    
    std::cout << "Printing contents of: " << filePath;
    std::string currentLine = "";
    std::ifstream myFile (filePath.c_str());
    if (myFile.is_open()) {
        while ( (std::getline (myFile, currentLine))) {
            std::cout << currentLine << "\n";
        } 
    }
    else {
       std::cout << "Could not print file"; 
    }
    myFile.close();
}
