 # PINNs Solver for Different Partial Differential Equations

## 1. Klein-Gordon Equation

### Case 1
Let $$\( a \in \mathbb{R} \)$$ and \( b > 0 \). The equation is:

$$
\left(\partial_t^2 - a^2 \nabla^2 + b \right)\psi(x,t) = 0, \quad (x,t) \in [1, 5] \times [0,T],
$$

with initial conditions:

$$
\psi(x,0) = a \cos\left(\frac{\pi}{2} x \right), \quad \psi_t(x,0) = b\mu \cos\left(\frac{\pi}{2}x\right),
$$

and Dirichlet boundary conditions:

$$
\psi(1,t) = \psi(5,t) = 0,
$$

where:

$$
\mu = \sqrt{b + \frac{a^2 \pi^2}{4}}.
$$

The exact solution is:

$$
\psi(x,t) = \cos\left(\frac{\pi x}{2}\right) \left(a \cos\left(\mu t\right) + b \sin\left(\mu t\right)\right).
$$

### Case 2
Let $$\( a \in \mathbb{R} \)$$ and $$\( b > 0 \)$$. The equation is:

$$
\left(\partial_t^2 - a^2 \nabla^2 + b \right)\psi(x,t) = 0, \quad (x,t) \in [0, 4] \times [0,T],
$$

with initial conditions:

$$
\psi(x,0) = a e^{-\frac{\pi x}{2}}, \quad \psi_t(x,0) = b\mu e^{-\frac{\pi}{2} x},
$$

and boundary conditions:

$$
\psi(0,t) = a \cos(\mu t) + b \sin(\mu t), \quad \psi(4,t) = e^{-2\pi}\left(a \cos(\mu t) + b \sin(\mu t)\right),
$$

where:

$$
\mu = \sqrt{b - \frac{a^2 \pi^2}{4}}.
$$

The exact solution is:

$$
\psi(x,t) = e^{-\frac{\pi}{2} x} \left( a \cos(\mu t) + b \sin(\mu t) \right).
$$

## 2. Lid-Driven Cavity Problem

The equations governing the lid-driven cavity problem are:

$$
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = -\frac{1}{\rho}\frac{\partial p}{\partial x} + \nu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right),
$$

$$
\frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} = -\frac{1}{\rho}\frac{\partial p}{\partial y} + \nu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} \right),
$$

$$
\frac{\partial^2 p}{\partial x^2} + \frac{\partial^2 p}{\partial y^2} = -\rho \left( \left(\frac{\partial u}{\partial x}\right)^2 + 2 \frac{\partial u}{\partial y}\frac{\partial v}{\partial x} + \left(\frac{\partial v}{\partial y}\right)^2 \right).
$$

The initial condition is:

$$
u, v, p = 0 \quad \text{everywhere},
$$

and the boundary conditions are:

- \( u = 1 \) at \( y = 2 \) (moving lid at the top boundary),
- \( u = v = 0 \) on all other boundaries (no-slip condition),
- $$\( \frac{\partial p}{\partial y} = 0 \) at \( y = 0 \) \textit{(bottom boundary, no vertical pressure gradient)}$$,
- \( p = 0 \) at \( y = 2 \) (pressure is zero at the top boundary),
- $$\( \frac{\partial p}{\partial x} = 0 \) at \( x = 0, 2 \) \textit{(no horizontal pressure gradient at the side walls)}$$.

