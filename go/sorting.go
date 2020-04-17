package algo

// BubbleSort returns a sorted list of integers using the bubble sort algorithm
func BubbleSort(elems []int) []int {
	if elems == nil {
		return nil
	}

	for mx := len(elems) - 1; mx >= 0; mx-- {
		for idx := 1; idx <= mx; idx++ {
			if elems[idx-1] > elems[idx] {
				elems[idx-1], elems[idx] = elems[idx], elems[idx-1]
			}
		}
	}
	return elems
}

// Selection returns a sorted slice using the selection sort algorithm
func Selection(elems []int) []int {
	if elems == nil {
		return nil
	}

	n := len(elems) - 1
	for i := 0; i <= n; i++ {
		maxIdx := i
		for j := i + 1; j <= n; j++ {
			if elems[j] < elems[maxIdx] {
				maxIdx = j
			}
		}
		// Now we swap between the min and current if they are different
		if maxIdx != i {
			elems[i], elems[maxIdx] = elems[maxIdx], elems[i]
		}
	}

	return elems
}

// InsertSort sorts a list of integers using the insert method
func InsertSort(elems []int) []int {
	if elems == nil {
		return nil
	}

	for current := 1; current < len(elems); current++ {
		item := elems[current]
		search_idx := current
		for ; search_idx > 0 && elems[search_idx-1] > item; search_idx-- {
			elems[search_idx] = elems[search_idx-1]
		}
		elems[search_idx] = item
	}
	return elems
}
