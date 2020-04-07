package algo

// BubbleSort returns a sorted list of integers using the bubble sort algorithm
func BubbleSort(elems []int) []int {
	if elems == nil {
		return nil
	}

	for mx := len(elems) - 1; mx >= 0; mx-- {
		for idx := 1; idx <= mx; idx++ {
			if elems[idx - 1] > elems[idx] {
				elems[idx - 1], elems[idx] = elems[idx], elems[idx - 1]
			}
		}
	}
	return elems
}
