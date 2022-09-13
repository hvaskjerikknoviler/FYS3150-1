#include<iostream>
#include<armadillo>
#include<string>
#include<fstream>
#include<iomanip>

arma::vec f(arma::vec);
arma::vec solve(int a, int b, int c, int n, arma::vec x, double h);


arma::vec f(arma::vec x){
  return 100*exp(-10*x);
}

arma::vec solve(int a, int b, int c, int n, arma::vec x, double h){
  arma::vec a_vec = arma::vec(n-1).fill(a);
  arma::vec b_vec = arma::vec(n).fill(b);
  arma::vec c_vec = arma::vec(n-1).fill(c);
  arma::vec v = arma::vec(n).fill(0);
  arma::vec g = f(x)*h*h;

  for (int i = 1; i < n; i++){
    b_vec[i] = b_vec[i] - a_vec[i]*c_vec[i-1]/b_vec[i-1];
    g[i] = g[i] - a_vec[i]*g[i-1]/b_vec[i-1];
  }

  v[n-1] = g[n-1]/b_vec[n-1];

  for (int i = n-1; i > 0; i--){
    v[i-1] = (g[i-1] - c_vec[i-1]*v[i])/b_vec[i-1];
  }
  return v;
}

int main(){
  int a = -1;
  int b = 2;
  int c = -1;
  int n = 10;
  double h = 1./n;
  arma::vec x = arma::linspace(0+1./(n+1), 1-1./(n+1), n);
  arma::vec x1 = arma::linspace(0, 1, n+2);
  arma::vec res = solve(a, b, c, n , x, h);
  arma::vec res1 = arma::vec(n+2).fill(0);
  std::cout << res << x << x1 << "\n";

  for (int i = 1; i < (n+1); i++){
    res1[i] = res[i-1];
  }

  std::string filename = "x_v.txt";

  std::ofstream ofile;
  ofile.open (filename);
  int width = 12;
  int prec = 4;
  for (int i = 0; i < (n+2); i ++){
  ofile << std::setw(width) << std::setprecision(prec) << std::scientific << x1(i)
  << std::setw(width) << std::setprecision(prec) << std::scientific << res1(i)
  << std::endl;
  }
  ofile.close();

  return 0;
}
