#!/usr/bin/env node
import TodoList, * as toDoList from "./todo/TodoList"
import {askQuestion} from './util'
import * as exercises from './exercises'

let quit = false;

async function launchTodo(){
  const todoList = new TodoList();
  await todoList.start();
}

async function smallExercises(){
  await exercises.start();
}

async function detectMenuAction(){
  let invalidChoice;
  do {
    invalidChoice = false;
    const choice = await askQuestion("Choice: ");
    switch(choice){
      case "1":
        await launchTodo();
        break;
      case "2":
        await smallExercises();
        break;
      case "0":
        quit = true;
        break;
      default:
        console.log("Invalid choice, try again.")
        invalidChoice = true;
        break;
    }
  } while(invalidChoice)
}

async function start(){
  while (!quit){
    console.log("Typescript assignment application - by Arne Cools")
    console.log("1: Launch to-do list application")
    console.log("2: Launch small exercises")
    console.log("0: Quit")
    await detectMenuAction()
  }
}


start();
