import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-player-summary',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss']
})

export class PlayerSummaryComponent implements OnInit {
  playerSummary: any;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getPlayerSummary();
  }

  getPlayerSummary(): void {
    const playerID = 1; 
    this.http.get(`http://127.0.0.1:8000/api/v1/playerSummary/${playerID}`)
      .subscribe({
        next: (data) => {
          this.playerSummary = data;
          console.log('Fetched Player Summary:', data);
        },
        error: (err) => {
          console.error('Failed to fetch player summary', err);
        }
      });
  }
}