import * as redis from 'redis'
export default class TodoRepository{
  client:redis.RedisClient;
  key:string;
  constructor() {
    this.client = redis.createClient();
    this.key = "todo";
  }

  writeTask(item:string){
    this.client.sadd(this.key, item);
  }

  deleteTask(item:string){
    this.client.srem(this.key, item);
  }

  async readTasks(){
    return new Promise<any[]>( resolve => this.client.multi()
    .scard(this.key)
    .smembers(this.key)
    .exec( (err, tasks) => {
        resolve(tasks[1]);
    }));
  }

}