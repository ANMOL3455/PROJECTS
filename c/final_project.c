//-------------------------------------------------------------
//after learning c programming up to file handling this is my final project
//here i have used my whole learning of last 2 years
//-------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "students.txt"

typedef struct {
    char username[50];
    char rollno[20];
    char course[50];
} Student;

void addStudent();
void viewStudents();
void searchStudent();
void deleteStudent();

int main() {
    int choice;
    while (1) {
        printf("\n--- Student Record System ---\n");
        printf("1. Add Student\n");
        printf("2. View All Students\n");
        printf("3. Search Student\n");
        printf("4. Delete Student\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar();  // clear newline from input buffer

        switch (choice) {
            case 1: addStudent(); break;
            case 2: viewStudents(); break;
            case 3: searchStudent(); break;
            case 4: deleteStudent(); break;
            case 5: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}

void addStudent() {
    FILE *fp;
    Student s;

    fp = fopen(FILENAME, "a"); // append mode, creates file if not exists
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    printf("Enter username: ");
    fgets(s.username, sizeof(s.username), stdin);
    s.username[strcspn(s.username, "\n")] = '\0'; // remove newline

    printf("Enter roll number: ");
    fgets(s.rollno, sizeof(s.rollno), stdin);
    s.rollno[strcspn(s.rollno, "\n")] = '\0';

    printf("Enter course: ");
    fgets(s.course, sizeof(s.course), stdin);
    s.course[strcspn(s.course, "\n")] = '\0';

    fprintf(fp, "%s,%s,%s\n", s.username, s.rollno, s.course);
    fclose(fp);
    printf("Student added successfully!\n");
}

void viewStudents() {
    FILE *fp;
    Student s;
    char line[200];

    fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        printf("No records found.\n");
        return;
    }

    printf("\n--- All Students ---\n");
    while (fgets(line, sizeof(line), fp)) {
        sscanf(line, "%49[^,],%19[^,],%49[^\n]", s.username, s.rollno, s.course);
        printf("Username: %s | Roll No: %s | Course: %s\n", s.username, s.rollno, s.course);
    }

    fclose(fp);
}

void searchStudent() {
    FILE *fp;
    Student s;
    char line[200], searchName[50];
    int found = 0;

    fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        printf("No records found.\n");
        return;
    }

    printf("Enter username to search: ");
    fgets(searchName, sizeof(searchName), stdin);
    searchName[strcspn(searchName, "\n")] = '\0';

    while (fgets(line, sizeof(line), fp)) {
        sscanf(line, "%49[^,],%19[^,],%49[^\n]", s.username, s.rollno, s.course);
        if (strcmp(s.username, searchName) == 0) {
            printf("Record found!\n");
            printf("Username: %s | Roll No: %s | Course: %s\n", s.username, s.rollno, s.course);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("No record found for username: %s\n", searchName);
    }

    fclose(fp);
}

void deleteStudent() {
    FILE *fp, *temp;
    Student s;
    char line[200], deleteName[50];
    int found = 0;

    fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        printf("No records found.\n");
        return;
    }

    temp = fopen("temp.txt", "w");
    if (temp == NULL) {
        printf("Error opening temp file!\n");
        fclose(fp);
        return;
    }

    printf("Enter username to delete: ");
    fgets(deleteName, sizeof(deleteName), stdin);
    deleteName[strcspn(deleteName, "\n")] = '\0';

    while (fgets(line, sizeof(line), fp)) {
        sscanf(line, "%49[^,],%19[^,],%49[^\n]", s.username, s.rollno, s.course);
        if (strcmp(s.username, deleteName) != 0) {
            fprintf(temp, "%s,%s,%s\n", s.username, s.rollno, s.course);
        } else {
            found = 1;
        }
    }

    fclose(fp);
    fclose(temp);

    remove(FILENAME);
    rename("temp.txt", FILENAME);

    if (found)
        printf("Record deleted successfully!\n");
    else
        printf("No record found for username: %s\n", deleteName);
}
