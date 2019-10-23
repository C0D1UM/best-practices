import TodoService from './services/todoService';
import {askQuestion} from '../util';

export default class TodoList{
  todoService: TodoService;
  quit: boolean;
  constructor() {
    this.todoService = new TodoService();
    this.quit = false;
  }
  
  async createNewItem(){
    let quit = false;
    console.log("Please enter the task you would like to add.")
    console.log("Enter a blank line to return to the menu.")
    do {
      let item: string;
      item = String(await askQuestion("New task: "));
      if(item != "") {
        this.todoService.addTask(item);
      }
      else quit = true;
    } while(!quit)
    
    
  }
  
  async viewAllItems(){
    console.log("All tasks:")
    const tasks = await this.todoService.getTasks();
    tasks.forEach((task, index) => {
      console.log(index + ":", task);
    });
  }
  
  async removeItem(){
    console.log("Enter the number of the task you want to delete:")
    const tasks = await this.todoService.getTasks();
    tasks.forEach((task, index) => {
      console.log(index + ":", task);
    });
    const choice: number = Number(await askQuestion("Task nr: "));
    if (isNaN(choice) || choice < 0 || choice >= tasks.length){
      console.log("Invalid choice");
    } else{
      this.todoService.removeTask(tasks[choice]);
    }
  }
  
  
  async detectMenuAction(){
    let invalidChoice;
    do {
      invalidChoice = false;
      const choice = await askQuestion("Choice: ");
      switch(choice){
        case "1":
          await this.createNewItem();
          break;
        case "2":
          await this.viewAllItems();
          break;
        case "3":
          await this.removeItem();
          break;
        case "0":
          this.quit = true;
          break;
        default:
          console.log("Invalid choice, try again.")
          invalidChoice = true;
          break;
      }
    } while(invalidChoice)
  }
  
  async start(){
      while (!this.quit){
        console.log("=====================================")
        console.log("============ TO-DO List =============")
        console.log("=====================================")
        console.log("1: Create new To-Do item")
        console.log("2: View all To-Do item")
        console.log("3: Remove a To-Do item")
        console.log("0: Quit")
        await this.detectMenuAction()
      }
      console.log("Goodbye and thank you for using the to-do list!");
  }
  
}


