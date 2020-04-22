package main

import (
	"encoding/csv"
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func IOReadDir(root string) ([]string, error) {
	var files []string
	fileInfo, err := ioutil.ReadDir(root)
	if err != nil {
		return files, err
	}

	for _, file := range fileInfo {
		files = append(files, file.Name())
	}
	return files, nil
}

// Define the function and accepting a string filepath and returning a [][]string value
func readCsv(filePath string) [][]string {
	// Open target file for reading, assign to 'in'
	in, err := os.Open(filePath)

	// NewReader returns a new Reader that reads from in.
	r := csv.NewReader(in)

	// Read the entire open file into the variable 'record'
	record, err := r.ReadAll()
	fmt.Println(record)
	// If err holds a value, then log a fatal error.
	if err != nil {
		log.Fatal(err)
	}

	os.Open(filePath + "CLEANSED", 'w')
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)

	return record
}

func main() {
	root := "./tables/"
	fmt.Println("Starting...")

	files, err := IOReadDir(root)

	if err != nil {
		fmt.Println("ERROR:")
		fmt.Println(err)
	}

	for _, file := range files {
		csvTable := readCsv(root + file)
		println(csvTable)
	}

	fmt.Println(files)

}
