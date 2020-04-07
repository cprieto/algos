package algo

import (
	"reflect"
	"testing"
)

var entry = []int{5, 1, 4, 2, 8}
var expected = []int{1, 2, 4, 5, 8}

func TestBubbleSortWithNilList(t *testing.T) {
	result := BubbleSort(nil)
	if result != nil {
		t.Errorf("Expected a nil list but got %v", result)
	}
}

func TestBubbleSortWithUnsortedList(t *testing.T) {
	if result := BubbleSort(entry); !reflect.DeepEqual(expected, result) {
		t.Errorf("Expected %v but got %v", expected, result)
	}
}

func TestBubbleSortSortedListIsSorted(t *testing.T) {
	if result := BubbleSort(expected); !reflect.DeepEqual(expected, result) {
		t.Errorf("Expected %v but got %v", expected, result)
	}
}

func TestSelectionSortUnsortedSliceReturnsSortedSlice(t *testing.T) {
	if result := Selection(entry); !reflect.DeepEqual(expected, result) {
		t.Errorf("Expected %v but got %v", expected, result)
	}
}

func TestSelectionSortSortedSliceReturnsSortedSlice(t *testing.T) {
	if result := Selection(expected); !reflect.DeepEqual(expected, result) {
		t.Errorf("Expected %v but got %v", expected, result)
	}
}

func TestSelectionSortNilReturnsNil(t *testing.T) {
	if result := Selection(nil); result != nil {
		t.Errorf("Expected nil but got %v", result)
	}
}
