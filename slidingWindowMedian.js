//morning algos
//sliding window median

//unfinished this doesnt work...

class Node {
    constructor(data){
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class Queue {
    constructor(){
        this.front = null;
        this.rear = null;
    }

    isEmpty(){
        if (!this.front){
            return true;
        }
        return false;
    }

    enqueue(data){
        let newNode = new Node(data);
        if (this.isEmpty()){
            this.front = newNode;
            this.rear = newNode;
        }
        else {
            this.rear.next = newNode;
            newNode.prev = this.rear;
            this.rear = newNode;
        }
    }

    dequeue(){
        this.front = this.front.next;
        this.front.prev = null;
    }

    //fix the sorting method...results in infinite loop
    //this doesn't sort correctly
    //selection sort, insertion sort, bubble sort
    // all sorting methods ^^^ in efficient
    sort(){
        let runner = this.front;
        
        while (runner.next){
        }
        
        console.log();
        this.printQueue();
    }

    // helper function
    printQueue() {
        var runner = this.front;
        if (this.front) {
            console.log("FRONT: " + this.front.data)
        }

        while (runner) {
            console.log(runner.data)
            runner = runner.next
        }
        if (this.rear) {
            console.log("REAR: " + this.rear.data)
        }
    }


    //finding the median of the window
    findMedian(){
        const temp = [];
        let runner = this.front;
        while (runner){
            temp.push(runner.data);
            runner = runner.next;
        }

        // temp.sort();

        for (let i = 0; i < temp.length; i++){
            for (let j = 0; j < temp.length - i - 1; j++){
                if (temp[j] > temp[j+1]){
                    [temp[j],temp[j+1]] = [temp[j+1],temp[j]];
                }
            } 
        }

        // console.log("WINDOW: ",temp);
        if (temp.length % 2 === 0){
            let average = null;
            average = (temp[temp.length/2 - 1] + temp[temp.length/2]) / 2;
            return average;
        }
        else {
            return temp[Math.floor(temp.length/2)];
        }
    }
}

/*
get the array
for loop through the array
enqueue first size
sort : either .sort or make your own sort
find median : if odd get the middle, if even average the middle two
output median
dequeue front and enqueue next in array

Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

 for( init queue with size k )

 for( traversing nums array )

*/

function slidingWindowMedian(arr, size){
    
    const window = new Queue();
    const output = [];

    //initializing the original window
    for (let i = 0; i < size; i++){
        window.enqueue(arr[i]);
    }
    
    //output median intial window
    output.push(window.findMedian())

    for (let j = size; j < arr.length; j++){
        window.dequeue();
        window.enqueue(arr[j]);
        output.push(window.findMedian());
    }

    return output;
}



// Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
// Input: nums = [1,2,3,4,2,3,1,4,2], k = 3

console.log(slidingWindowMedian([1,3,-1,-3,5,3,6,7], 4));

// slidingWindowMedian([1,2,3,4,2,3,1,4,2], 4);