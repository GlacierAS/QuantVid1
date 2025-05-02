"I think I can safely say that nobody understands quantum mechanics" — _Richard P. Feynman_
$$-13.6eV.$$
If you are a science student, I am sure you somewhat familiar with this number. If you may recall, it might have appeared in your high school chemistry class, or perhaps in a introductory physics class first learning about what does the atom looks like; Perhaps it is out of curiosity that you asked your teacher "what is the energy of an electron" and what you get is this mysterious number. Or perhaps you have seen the energy level quation,
$$
\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)
$$
in you waves mechanic class. 

Now this equation looks clean, but if you are a little more involved in the physics community, you might know that getting this equation might not be the easiest task. Well, to be precise, to obtain this equation we need to "solve the Schrödinger equation for hydrogen atom". 

If you are confused, that is ok. Physics college students takes years of class after high school to prep for quantum mechanics, and in particular for me, McGill, I find the problem hard even after all these course, it was long, several pages of derivation, and to make it worse it was not taught in the first, but actually the second quantum mechanics course. 

However, I do not think this is impossible to simplify it to a level that can be easily understood by people with little scientific background, in a more than hand wavy, but far from rigorous way. You just need to know some very simple physics, some basic calculus, and do a few algebraic manipulation tricks. And if you are a physics student looking to review some quantum mechanics, I hope this video also help you as well.

This will be a multi part video series that start from the big picture of quantum mechanics, and goes into finer details into by solving an actual well known quantum mechanic problem.
1. In part one, which is this video, will be a overview of some most important concept of quantum mechanics. This might be a overwhelming video, so I recommend slowing down and break it into sections. I will first introduce enough background knowledge you need to know to "solve the Schrödinger equation for hydrogen atom".


# Quantum State and Wave function
Now lets begin with some big picture of quantum mechanics. We need to "solve the Schrödinger equation", but what does it mean by solving it? 

Before we begin QM, I want you to think about something rudimental, something too simple that might often been overlooked. I am asking how does a physicist might do to describe some every day object?

We can do it in three steps
1. We will first assign properties to the object, for example, an apple might be classified where the apple is located at, and where it is going to. 
2. We need to get some coordinate system, like for example if we are interested its position, we might use three basis vectors to assign a 3D cartesian coordinate system. Maybe another momentum coordinate system attached to the apple telling us where it is going. Setting up the coordinate system allow us to represent the property we are interest in some mathematical way, like $\text{Apple}_{\text{position}}=(x,y,z)$, a set of numbers. 
3. We make measurements. For example, we say $\text{Apple}_{\text{position}}=(3,1,2)$ we meant the apple is located three units along the  $x$ axis $x\to 3$, one units along the $y$ axis $y\to2$, and 2 unit along the z axis with respect to the origin. Here we simply need to just read off the coordinate system.


Now begin our exploration in the quantum world, I want you to imagine two objects, a regular apple like the one we were describing, and a quantum apple, which I will describe in a quantum manner using above steps; and just for the sake of simplicity, I am going to reduce the position and momentum dimension to $1$. 
## Step 1: Representing Quantum Object
In the quantum world, quantum objects, like our quantum apple. are governed by what is called a quantum state, we generally use angled bracket like this 
$$\ket{\psi}$$
to denote it. A state is like an object we were talking about. We have properties like position, momentum, energies, etc. 

_A state is an abstract notation of a quantum object, contains every property we are interested in._
### What are these quantities?
But I want to mention something different here. In QM, there are in fact three kinds of properties base on values it take: 
1. Properties that can take up finite number of value, like spin, which we wont discuss here.
2. Properties that nature only allow taking up discrete value, for example, orbital angular momentum.
3. Properties allowing to take up any value we have, like position and momentum.
When I talk about properties that are discrete, I really meant it. Nature is very biased, and there are certain values nature is biased towards that allow us to take on. For example, we can never have a angular momentum value of $3.02\hbar$ at any situation. Angular momentum takes on values of $\dots,-2\hbar, -\hbar, 0, \hbar, 2\hbar,\dots$ or $\dots,-\frac{3}{2}\hbar, -\frac{1}{2}\hbar, 0, \frac{1}{2}\hbar, \frac{3}{2}\hbar,\dots$. There are of course more limits to them depending on the scenario, but other then these value, nature do not allow them at all. PERIOD.

We call the value we are allowed to take associated with a physical property a eigenvalue.

A more formal definition of this subtlety is that every physical property has its representation in some extended Hilbert space as a finite, countably infinite, or uncountably infinite set of basis vector called eigenvectors associated with the eigenvalue, with each eigenvalue representing some measurable value. Of course, this is worthy of half semester of material in a rigorous QM class, so I wont get into this formalism.

I have to emphasize on the energy property of an particle. Energy depends on many factors, sometimes position (potential energy), sometime linear momentum, and sometime angular momentum. Sometime energy can be continueous if its dependencies are continueous. But if energy depends on some discrete quantity, it has to be discrete. Now looking back, as you may now realize, the energy levels of an electron is discrete.
$$
\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)
$$
_$^{\dagger}$Often time not all values of are allowed. The allowed values are called eigenvalues._
## Step 2: Setup coordinate system
Now the second step is to set up a coordinate. In quantum mechanics we can mathematically represent a quantum state living in some coordinate system. We will do so it by sticking this leftward facing angle bracket known as a bra 
$$\bra{x}$$
to it, similarly if we want to represent its momentum, we stick a momentum bra $\bra{p_{x}}$ for momentum. This give us some wave function:
$$
\braket{ x |\psi  }=\psi(x).
$$
In QM notation, you should read this as, given some particle $\ket{\psi}$, when we try to figure out the $x$ coordinate, we get.... wait, what? is that... a function... that depends on $x$???

This is weird.... Think about a single dimension in classical system. When we talk about the location of an apple on the x axis, we are expecting things like $x\to3$ with momentum $p_{x}\to5$. We are expecting a number that describe them. It wouldn't make sense when we say the particle is at position $x \overset{\text{wtf???}}{\to}\left(  \frac{m\omega}{\pi\hbar} \right)^{1/4} \exp\left( -\frac{m\omega x^2}{2\hbar} \right)=\psi(x)$ and having a momentum of $p_{x} \overset{\text{wtf???}}{\to}\left( \frac{1}{\pi m \hbar \omega} \right)^{1/4} \exp\left( -\frac{p_{x}^2}{2m\hbar\omega} \right)=\psi(p_{x})$. This is definitely uncharted territory, because we have never seen a function used to represent a property, as opposed of single value. Our next step is to figure out why are wave functions necessary, and what do they mean?


_When we establish a coordinate system for some property, these properties are not directly represented by a number, instead, they are represent as a wave function._
### Uncertainty in measurements - Reason why we need wave function.
The thing is, when we think of classical mechanic, representing an object in a coordinate and making a measurement base on it is a seamless process. If we know it is at position 3, when we measure it, we are guarantee to have 3. In quantum mechanics, this is not the case. There is some sort of inherent randomness when given a measurement. The reason of which is because certain quantum properties are sometime not compatible with each other, like position and momentum. For example, if we are given position coordinate system and a momentum coordinate system, measuring position will change the subsequent measurement of momentum and vice versa. You might have heard about Heisenberg uncertainty principle, the most famous one is
$$
\Delta x\Delta p_{x} \ge \frac{\hbar}{2}
$$
This is just one of many uncertainty relations. Though you may need to take some time to interpret equation for a more formal look, an important result is that __for two incompatible property of an quantum object, maximum certainty in a single quantity means maximum uncertainty in the other__. So here, if I know the exact position of our quantum apple, then I will have no idea what the momentum is. The takeaway is measurement are not always definite, and source of randomness comes from __incompatibility__ of properties. I hope this motivates why we should not really assign exact quantity to properties. And we will see how wave function work in the next section.

## Step 3: Measurements
Now the last step is to "make a measurement" or "extract the data". This is the perhaps the most confusing part of quantum mechanics. So feel free to pause and rewind if you wish.

Previous we have discussed the the randomness in measurement, it is particularly useful to represent properties using functions $\psi(x)$ and $\psi(p_{x})$, in the sense that these function shall relate to the probability of getting value associated with the properties of our quantum apple; and in particular, the wave function squared is a probability density function. This is called Born's interpretation.
$$
\int_{a}^b|\psi(x)|^2dx=\text{Probability of getting measuremt of } x \text{ in range }[a,b] 
$$
And similarly for the momentum,
$$
\int_{a}^b|\psi(p_{x})|^2dp_{x}=\text{Probability of getting measuremt of } p \text{ in range }[a,b] 
$$
I do want to make a few remarks here. 
1. Because the above represents a probability, it is most natural to require $$
\int_{-\infty}^\infty|\psi(x)|^2dx=1
$$That is, sum of all probability across all trail to be $1$. This often means that we need to multiply $\psi(x)$ by some constant to ensure the above is satisfied. As we will see later, this property is not always automatically satisfied, and enforcing this equation is called normalizing the wave function. 
2. $\psi(x)$ in most of time is generally a complex function. That means this function might involve this weird number $\sqrt{ -1}=i$. Having complex number involved is very fundamental to quantum mechanics, and I understand it is awkward to first approach idea how $i$ comes in play in physics. But since complex number can be represented as a real vector, we can think about it as some handy tool to simplify the calculation, avoiding us getting into the algebraic mess of some higher dimensional real Hilbert space. Again, if you didn't understand what I am yapping about, don't worry about it too much.
### How are the measurement carried out?
Measurement are done mathematically by placing what we called _operator_ next to the state or wave function. These are the little hats on properties.
$$
\hat{x}\ket{\psi}  \text{ or }\hat{x}\psi(x)
$$
We can of course, do all kinds of probability measurement using them. But these will not be our focus today.

I want to mention, a very subtle but useful way to think about the probabilistic nature of measurement value here. Since eigenvalues represents all possible outcome of a measurement, we can imagine a pool of quantum states under some physical quantity, for example position, and for each of these state we demand that when measured, it will guarantee, with 100% certainty, yield the same eigenvalue every time. These are called eigenstates and eigenfunctions which represent using a ket and put the eigenvalue inside it.
$$
\ket{x}=\{ \ket{1} ,\ket{2} ,\ket{0.21},\ket{1/3},   \dots\} _{\leftarrow \text{ actuelly uncountable but you get the point}}
$$
As a side note I want to briefly that we can indeed have eigenstates corresponds to multiple physical properties as long as they are compatible to each other, because otherwise, the uncertainty principle kicks in. We wont get into too much details for that though.
$$
\ket{x,???}=\{ \ket{1,???_{1}} ,\ket{2,???_{2}} ,\ket{0.21,???_{3}},\ket{1/3, ???_{4}},   \dots\} _{\leftarrow \text{ actuelly uncountable but you get the point}}
$$

To represent measurement of a eigenstate giving 100% certainty, we write what is called the eigenvalue equation.
$$
\begin{align}
 & \hat{x}\ket{x_{0}}=x_{0}\ket{x_{0}}   & \implies &  \text{ e.g. }\hat{x}\ket{5} = 5\ket{5} \\  & \text{In position coordinate:} &  \\

 & \hat{x}\psi(x)=x \psi(x)
\end{align}
$$
Eigenvalue equations are interesting, because these are differential equation, that when solved, actually tells us what the eigenvalue and eigenstates are. You will see later that a variance of Schrödinger equation is just a eigenvalue equation.

Now back to our quantum apple, we know the its wave function is just a probability distribution of all possible position eigenstates and eigenvalues, under the standard theory of quantum mechanics called the Copenhagen interpretation, we would say our wave function, that is our quantum apple, exists simultaneously in all possible position. That is, it is a superposition of eigenstates. 

We can think about making a measurement, we should really think about sampling from our the pool of eigenstates. 

There is another important quirkiness of quantum mechanics is once you made a sample, the wave function now __becomes__ eigenstates, and now repeated measurement will give the respected eigenvalue. This should make intuitive sense, because other wise there would be no meaning of measurement. For the Copenhagen enthusiasts, this process is known as collapsing a wave function.
# Schrödinger equation
Our last section of this video we will briefly discuss at the Schrödinger equation. This is the last piece of puzzle for our goal of finding the energy levels of an electron. I store This is the equivalence of Newton's second law,
$$
\vec{F}=m\frac {d^2x}{dt^2}=-\frac{dV}{dx}
$$
in QM. It is a complex equation that states, 
$$
i \hbar \frac{\partial}{\partial t} \ket{\psi(t)} = \hat{H} \ket{\psi(t)}
$$
In position coordinate system.
$$
i \hbar \frac{\partial}{\partial t} \psi(x, t) = \hat{H}\psi(x, t)
$$
This is the equation that tells us how a particle with wave function $\psi(x,t)$ evolve with time. We do not expect the energy of a electron will change with time though, so we can simplify this equation by dropping the time factor. 
$$
\begin{align}
\hat{H}\ket{\psi} & =E\ket{\psi}   \\
\hat{H} \psi(x) &  = E \psi(x)
\end{align}
$$
Look at that! It becomes the eigenvalue equation. How we should read this equation is that, $\hat{H}$ here is the hamiltonian operator, it is used to measure the total energy of a particle. When we apply that onto the energy eigenstate, we will get the energy eigenvalue. Since electron energy is are discrete, what we mean by finding the energy levels of electron is really just finding the allowed energy eigenvalues, and eventually what we can achieve is a general pattern of how we compute these energies. And we know exactly how to do it - solving this eigenvalue equation which we will do in the next video.


# In person closure
Hi, I am Yichen. We have discussed quite a lot today about the big picture of quantum mechanics, explaining what a quantum state, what is wave function, why we need it, we talked about eigenstates and the eigenvalue equation and in particular, the Schrödinger equation. ... etc..