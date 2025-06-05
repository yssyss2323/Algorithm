#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define LEN 15

int year(char date[]);

int month(char date[]);

int day(char date[]);

bool compare(char date1[], char date2[]);

int main() {
    char date[LEN];
    scanf("%s", date);

    int n;
    scanf("%d", &n);
    
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        char curr[LEN];
        scanf("%s", curr);

        if (compare(date, curr)) cnt += 1;
        
    }
    printf("%d", cnt);
    return 0;
}

int year(char date[]) {
    int year = 0;
    for (int i = 0; i < 4; i++) {
        int tmp = date[i] - '0';
        year = year * 10 + tmp;
    }
    return year;
}

int month(char date[]) {
    int month = 0;
    for (int i = 5; i < 7; i++) {
        int tmp = date[i] - '0';
        month = month * 10 + tmp;
    }
    return month;
}

int day(char date[]) {
    int day = 0;
    for (int i = 8; i < 10; i++) {
        int tmp = date[i] - '0';
        day = day * 10 + tmp;
    }
    return day;
}

bool compare(char date1[], char date2[]) {
    int year1, year2, month1, month2, day1, day2;
    year1 = year(date1);
    year2 = year(date2);
    month1 = month(date1);
    month2 = month(date2);
    day1 = day(date1);
    day2 = day(date2);

    if (year1 > year2) return false;
    else if (year1 < year2) return true;
    else {
        if (month1 > month2) return false;
        else if (month1 < month2) return true;
        else {
            if (day1 > day2) return false;
            else return true;
        }
    }
}