package algo

// BubbleSort returns a sorted list of integers using the bubble sort algorithm
func BubbleSort(elems []int) {
	for mx := len(elems) - 1; mx >= 0; mx-- {
		for idx := 1; idx <= mx; idx++ {
			if elems[idx-1] > elems[idx] {
				elems[idx-1], elems[idx] = elems[idx], elems[idx-1]
			}
		}
	}
}

// SelectionSort returns a sorted slice using the selection sort algorithm
func SelectionSort(elems []int) {
	n := len(elems) - 1
	for i := 0; i < n; i++ {
		maxIdx := i
		for j := i + 1; j < n; j++ {
			if elems[j] < elems[maxIdx] {
				maxIdx = j
			}
		}

		// Now we swap between the min and current if they are different
		elems[i], elems[maxIdx] = elems[maxIdx], elems[i]
	}
}

// InsertionSort sorts a list of integers using the insert method
func InsertionSort(elems []int) {
	for j := 1; j <= len(elems)-1; j++ {
		ins := elems[j]
		i := j - 1
		for i >= 0 && ins < elems[i] {
			elems[i+1] = elems[i]
			i = i - 1
		}
		elems[i+1] = ins
	}
}

// CountingSort sorts a list of integers using the counting method
func CountingSort(elems []int, max int) {
	n := len(elems)
	temp := make([]int, max+1)
	for i := 0; i < n; i++ {
		temp[elems[i]]++
	}

	prev := 0
	for i := 0; i < max+1; i++ {
		if temp[i] != 0 {
			temp[i] += prev
			prev = temp[i]
		}
	}

	output := make([]int, n)
	for _, v := range elems {
		pos := temp[v] - 1
		temp[v]--
		output[pos] = v
	}

	for i, v := range output {
		elems[i] = v
	}
}
