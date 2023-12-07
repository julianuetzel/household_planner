import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { List } from '../lists/lists';
import { Observable, map, shareReplay } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ListServiceService {

  constructor(private http: HttpClient) { }

  public get_lists(): Observable<List[]> {
    let lists = this.http.get<List[]>("http://127.0.0.1:5000/lists").pipe(
      shareReplay()
    )
    return lists;
  }
}

