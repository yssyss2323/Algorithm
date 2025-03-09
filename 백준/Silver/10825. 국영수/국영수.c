#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LEN 10

typedef struct {
    int kor;
    int eng;
    int math;
    char name[MAX_LEN + 1];
} Student;

int compare(const void* student1, const void* student2) {
    const Student* s1 = (const Student*)student1;
    const Student* s2 = (const Student*)student2;

    if (s1->kor > s2->kor) return -1;
    else if (s1->kor < s2->kor) return 1;

    if (s1->eng < s2->eng) return -1;
    else if (s1->eng > s2->eng) return 1;

    if (s1->math > s2->math) return -1;
    else if (s1->math < s2->math) return 1;

    return strcmp(s1->name, s2->name);
}

int main() {
    int n;
    scanf("%d", &n);

    Student class[n];
    for (int i = 0; i < n; i++){
       scanf("%s %d %d %d", class[i].name, &class[i].kor, &class[i].eng, &class[i].math);
    }
    
    qsort(class, n, sizeof(Student), compare);

    for (int i = 0; i < n; i++){
        printf("%s\n", class[i].name);
    }
    return 0;
}