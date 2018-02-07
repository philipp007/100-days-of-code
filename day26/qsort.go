package main

import "fmt"

func qsort(arr []int) []int {
	if (len(arr) == 0) {
		return []int {}
	}

	if (len(arr) == 1) {
		return []int { arr[0] }
	}

	if (len(arr) == 2) {
		if (arr[0] > arr[1]) {
			return []int { arr[1], arr[0] }
		} else {
			return []int { arr[0], arr[1] }
		}
	}

	pivot := arr[0]
	var left []int
	var right []int

	for i := 1; i < len(arr); i++ {
		if arr[i] <= pivot {
			left = append(left, arr[i])
		} else {
			right = append(right, arr[i])
		}
	}

	return append(append(qsort(left), pivot), qsort(right)...)
}

func main() {
	arr := []int {5, 2, 17, -10, 20, 23, -1, -10, 1000}
	fmt.Println(qsort(arr))
}