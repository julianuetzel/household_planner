import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListComponent } from './list/list.component';
import { NoteComponent } from './note/note.component';
import { NewListComponent } from './new-list/new-list.component';
import { NewNoteComponent } from './new-note/new-note.component';
import { ListViewComponent } from './list-view/list-view.component';

const routes: Routes = [
  {path: 'list/:id', component: ListComponent },
  {path: 'note/:id', component: NoteComponent },
  {path: 'newList', component: NewListComponent },
  {path: 'newNote', component: NewNoteComponent },
  {path: '', component: ListViewComponent},
  {path: '', redirectTo: '/', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
