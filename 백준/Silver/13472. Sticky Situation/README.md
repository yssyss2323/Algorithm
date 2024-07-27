# [Silver IV] Sticky Situation - 13472 

[문제 링크](https://www.acmicpc.net/problem/13472) 

### 성능 요약

메모리: 33164 KB, 시간: 44 ms

### 분류

기하학, 그리디 알고리즘, 수학, 정렬

### 제출 일자

2024년 7월 27일 13:15:30

### 문제 설명

<p>While on summer camp, you are playing a game of hide-and-seek in the forest. You need to designate a “safe zone”, where, if the players manage to sneak there without being detected, they beat the seeker. It is therefore of utmost importance that this zone is well-chosen.</p>

<p>You point towards a tree as a suggestion, but your fellow hide-and-seekers are not satisfied. After all, the tree has branches stretching far and wide, and it will be difficult to determine whether a player has reached the safe zone. They want a very specific demarcation for the safe zone. So, you tell them to go and find some sticks, of which you will use three to mark a non-degenerate triangle (i.e. with strictly positive area) next to the tree which will count as the safe zone. After a while they return with a variety of sticks, but you are unsure whether you can actually form a triangle with the available sticks.</p>

<p>Can you write a program that determines whether you can make a triangle with exactly three of the collected sticks?</p>

### 입력 

 <p>The first line contains a single integer N, with 3 ≤ N ≤ 20 000, the number of sticks collected. Then follows one line with N positive integers, each less than 2<sup>60</sup>, the lengths of the sticks which your fellow campers have collected.</p>

### 출력 

 <p>Output a single line containing a single word: possible if you can make a non-degenerate triangle with three sticks of the provided lengths, and impossible if you can not.</p>

