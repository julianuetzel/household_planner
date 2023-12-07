import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatTabsModule} from '@angular/material/tabs';
import {MatCardModule} from '@angular/material/card';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatListModule} from '@angular/material/list';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatTooltipModule} from '@angular/material/tooltip';
import { ListsComponent } from './lists/lists.component';
import { NotesComponent } from './notes/notes.component';
import { ListComponent } from './list/list.component';
import { NoteComponent } from './note/note.component';
import { NewListComponent } from './new-list/new-list.component';
import { NewNoteComponent } from './new-note/new-note.component';
import { ListViewComponent } from './list-view/list-view.component';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ListsComponent,
    NotesComponent,
    ListComponent,
    NoteComponent,
    NewListComponent,
    NewNoteComponent,
    ListViewComponent,
  ],
  imports: [
    RouterOutlet,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTabsModule,
    MatCardModule,
    MatCheckboxModule,
    MatListModule,
    MatGridListModule,
    MatButtonModule,
    MatIconModule,
    MatTooltipModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
