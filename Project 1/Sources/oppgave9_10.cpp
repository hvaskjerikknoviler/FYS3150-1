#include<iostream>
#include<armadillo>
#include<string>
#include<fstream>
#include<iomanip>
#include<math.h>
#include<chrono>

arma::vec f(arma::vec x) {
  return 100*exp(-10*x);
}

int main(){
  auto t1 = std::chrono::high_resolution_clock::now();
  int a = -1;
  int b = 2;
  int c = -1;
  double n = std::pow(10,6);
  arma::vec b_t = arma::vec(n).fill(2);
  arma::vec x = arma::linspace(0+1./(n+1),1-1./(n+1),n);
  double h = 1./n;
  arma::vec g = f(x)*h*h;
  arma::vec g_t = f(x)*h*h;
  arma::vec v = arma::vec(n).fill(0);

  for (int i=1; i<n ;i++){
    b_t[i] = 2 - 1./b_t[i-1];
    g_t[i] = g[i] + g_t[i-1]/b_t[i-1];
  }
  v[n-1] = g_t[n-1]/b_t[n-1];
  for (int i = (n-1); i >= 1;i--){
    v[i-1] = (g_t[i-1]+v[i])/b_t[i-1];
  }
  auto t2 = std::chrono::high_resolution_clock::now();
  double duration_seconds = std::chrono::duration<double>(t2-t1).count();

  std::cout << duration_seconds << "\n";

  return 0;
}
