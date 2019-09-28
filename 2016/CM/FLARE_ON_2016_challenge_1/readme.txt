string = (int)"x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q"; //string[0]
WriteFile (GetStdHandle(0xFFFFFFF5), "Enter password:\r\n", 18,  &NumberOfBytesWritten, 0);
ReadFile  (GetStdHandle(0xFFFFFFF6), &Buffer,               128, &NumberOfBytesWritten, 0);
input = (int)process_1((int)&Buffer, NumberOfBytesWritten - 2);

if(process_2(input, string) == 0){
	puts("You win");
}

//lpNumberOfBytesRead 与 nNumberOfBytesToRead 的区别

read the practical malware analysis Page#290