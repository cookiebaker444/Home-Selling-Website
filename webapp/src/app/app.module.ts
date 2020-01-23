import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { LoginPage } from './loginPage/login.component';
import { DashboardPage } from './dashboardPage/dashboard.component';
import { TopbarComponent } from './topbar/topbar.component';
import { ApiService } from './api.service';
import { MapService } from './map.service';

@NgModule({
  imports:[
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    RouterModule.forRoot([
      {path: '', component: LoginPage},
      {path:'dashboard',component:DashboardPage}
    ])
  ],

  declarations: [
    AppComponent,
    LoginPage,
    DashboardPage,
    TopbarComponent
  ],
  bootstrap:    [ AppComponent ],
  providers: [ ApiService, MapService ]
})
export class AppModule { }
