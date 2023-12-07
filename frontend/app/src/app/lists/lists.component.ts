import { Component, OnInit } from '@angular/core';
import { ThemePalette } from '@angular/material/core';
import { LISTS } from './lists.mockdata';
import { ListServiceService } from '../services/list-service.service';
import { List } from './lists';

@Component({
  selector: 'app-lists',
  templateUrl: './lists.component.html',
  styleUrls: ['./lists.component.scss']
})
export class ListsComponent implements OnInit{
  
  constructor(public listService: ListServiceService) { }

  lists: List[] = [];
  color: ThemePalette = 'primary';


  ngOnInit(): void {
    this.get_lists();
  }

  get_lists(): void {
    this.listService.get_lists().subscribe(
      lists => this.lists = lists
    )
  }

  checked(status: number): boolean {
    if(status == 0) return false;
    return true;
  }
}

