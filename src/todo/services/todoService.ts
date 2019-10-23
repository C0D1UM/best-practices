import TodoRepository from "../repositories/todoRepository";
export default class TodoService{
  todoRepository: TodoRepository;
  constructor() {
    this.todoRepository = new TodoRepository();
  }


  addTask(item:string){
    this.todoRepository.writeTask(item);
  }

  removeTask(item:string){
    this.todoRepository.deleteTask(item);
  }

  async getTasks(){
    return await this.todoRepository.readTasks();
  }

}