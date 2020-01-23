import { Component} from '@angular/core';
import {QUESTION_LIST} from '../constants';
import { ApiService } from '../api.service';
import { MapService } from '../map.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardPage {
  private QUESTION_LIST = QUESTION_LIST;
  private filters = {};
  private results = [];
  private submitted = false;
  private showFilter = true;
  private loadingResults = false;
  private viewLimit = 0;
  private eachViewLimit = 20;
  private clicked = 0;

  constructor(private apiService: ApiService, private mapService: MapService) {
    Object.keys(QUESTION_LIST).forEach((key) => {
      this.filters[key] = false;
    });
  }

  setMapCenter(result) {
    for (let i = 0; i < this.results.length; i++) {
      if (!this.results[i].marker) {
        break;
      }
      this.results[i].marker.setZIndex(this.results.length - (i + 1));
    }
    this.mapService.setCenter(result.latitude, result.longitude);
    result.marker.setZIndex(this.results.length);
  }

  increaseLimit() {
    let setMapCenter = this.setMapCenter;
    let vm = this;
    this.results.slice(this.viewLimit, this.viewLimit + this.eachViewLimit).forEach((result, index) => {
      result.marker = this.mapService.addMarker(result.latitude, result.longitude, (index + 1 + this.viewLimit).toString(), this.results.length - (index + 1 + this.viewLimit));
      result.marker.addListener('click', this.setMapCenter.bind(this, result))
    });
    this.setMapCenter(this.results[this.viewLimit]);
    this.viewLimit += this.eachViewLimit;
  }

  submit() {
    this.submitted = true;
    this.showFilter = false;
    this.loadingResults = true;
    this.viewLimit = 0;
    this.clicked = 0;
    this.mapService.initMap();
    this.apiService.getResults(this.filters)
        .subscribe(
            response => {
              this.results = response && response['housingData'] || [];
              this.increaseLimit();
              this.loadingResults = false;
            },
            error => {
              alert('error happened');
              this.results = [];
              this.loadingResults = false;
            }
        );
  }
}