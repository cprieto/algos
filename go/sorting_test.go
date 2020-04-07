package algo

import (
	"reflect"
	"testing"
)

func TestBubbleSortWithNilList(t *testing.T) {
	result := BubbleSort(nil)
	if result != nil {
		t.Errorf("Expected a nil list but got %v", result)
	}
}

func TestBubbleSortWithUnsortedList(t *testing.T) {
	expected := []int{1, 2, 4, 5, 8}
	result := BubbleSort([]int{5, 1, 4, 2, 8})
	if !reflect.DeepEqual(expected, result) {
		t.Errorf("Expected %v but got %v", expected, result)
	}
}
