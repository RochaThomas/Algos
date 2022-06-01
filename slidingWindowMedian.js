//morning algos
//sliding window median

//unfinished this doesnt work...

class Node {
    constructor(data){
        this.data = data;
        this.position = null;
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
            newNode.position = 0;
        }
        else {
            this.rear.next = newNode;
            newNode.prev = this.rear;
            this.rear = newNode;
            newNode.position = newNode.prev.position + 1;

        }
    }

    //fix the sorting method...results in infinite loop
    //this doesn't sort correctly
    //selection sort, insertion sort, bubble sort
    // all sorting methods ^^^ in efficient
    sort(){
        let runner = this.front;
        
        while (runner.next){
            let back = runner.next;
            let val = runner.next;
            while (val){
                if (val.prev === null || back.data > val.prev.data){
                    const temp = back.position;
                    back.position = val.position;
                    val.position = temp;
                    break;
                }
                else {
                    val = val.prev;
                }
            }
            console.log();
            this.printQueue();
            console.log();
            runner = runner.next;
        }
        
        console.log();
        this.printQueue();
    }

    // helper function
    printQueue() {
        // var runner = this.front;
        // if (this.front) {
        //     console.log("FRONT: " + this.front.data)
        // }

        // while (runner) {
        //     console.log(runner.data)
        //     runner = runner.next
        // }
        // if (this.rear) {
        //     console.log("REAR: " + this.rear.data)
        // }

        let runner = this.front;

        while (runner){
            console.log("data:", runner.data, " ---- position:", runner.position);
            runner = runner.next;
        }

    }
}

// function slidingWindowMedian(nums, k){
//     let output = [];
//     if (k % 2 === 0){
//         const shift = k / 2 - 1;
//         for (let i = shift; i < nums.length - shift - 1; i++){
//             output.push((nums[i] + nums[i + 1]) / 2);
//         }
//     }
//     else {
//         const shift = Math.floor(k/2);
//         for (let i = shift; i < nums.length - shift; i++){
//             output.push(nums[i]);
//         }
//     }
//     return output;
// }

// console.log(slidingWindowMedian([1,3,-1,-3,5,3,6,7], 3));

var window = new Queue();

window.enqueue(1);
window.enqueue(3);
window.enqueue(-1);
window.enqueue(-3);
window.enqueue(5);
// window.printQueue();

window.sort();