package algo

import (
	"reflect"
	"testing"
)

var expected = []int{1, 2, 4, 5, 8}

type testFunc func(elems []int)

func tester(f testFunc, t *testing.T) {
	entry := []int{5, 1, 4, 2, 8}
	f(entry)
	if !reflect.DeepEqual(entry, expected) {
		t.Errorf("Expected %v but got %v\n", expected, entry)
	}
}

func TestBubbleSort(t *testing.T) {
	tester(BubbleSort, t)
}

func TestInsertionSort(t *testing.T) {
	tester(InsertionSort, t)
}

func TestSelectionSort(t *testing.T) {
	tester(SelectionSort, t)
}

func TestCountingSort(t *testing.T) {
	entry := []int{5, 1, 4, 2, 8}
	CountingSort(entry, 8)
	if !reflect.DeepEqual(entry, expected) {
		t.Errorf("Expected %v but got %v\n", expected, entry)
	}
}

func BenchmarkBubbleSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		entry := []int{24, 22, 4, 5, 15, 10, 23, 0, 13, 7, 2, 19, 3, 21, 6, 17, 14, 20, 18, 8, 1, 12, 16, 9, 11}
		BubbleSort(entry)
	}
}

func BenchmarkInsertionSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		entry := []int{24, 22, 4, 5, 15, 10, 23, 0, 13, 7, 2, 19, 3, 21, 6, 17, 14, 20, 18, 8, 1, 12, 16, 9, 11}
		InsertionSort(entry)
	}
}

func BenchmarkSelectionSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		entry := []int{24, 22, 4, 5, 15, 10, 23, 0, 13, 7, 2, 19, 3, 21, 6, 17, 14, 20, 18, 8, 1, 12, 16, 9, 11}
		SelectionSort(entry)
	}
}

func BenchmarkCountingSort(b *testing.B) {
	for i := 0; i < b.N; i++ {
		entry := []int{24, 22, 4, 5, 15, 10, 23, 0, 13, 7, 2, 19, 3, 21, 6, 17, 14, 20, 18, 8, 1, 12, 16, 9, 11}
		CountingSort(entry, 24)
	}
}
