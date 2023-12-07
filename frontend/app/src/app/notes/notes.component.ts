import { Component } from '@angular/core';
import { NOTES } from './notes.mockdata';


@Component({
  selector: 'app-notes',
  templateUrl: './notes.component.html',
  styleUrls: ['./notes.component.scss']
})
export class NotesComponent {
  notes = NOTES;
}
