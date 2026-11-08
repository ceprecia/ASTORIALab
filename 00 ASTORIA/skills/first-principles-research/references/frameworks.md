# First-principles framework cards

Select cards by the mathematical structure of the question. Each card separates an identity or physical constraint from assumptions needed to make a model usable. A framework can expose an ambiguity, a computable quantity, or a discriminating observation; that alone does not establish an open scientific question.

The numerical examples below are constructed teaching cases. Published applications are identified separately. These cards contain the working definitions and sources needed to use them independently.

## Contents

1. [Probability conservation and currents](#1-probability-conservation-and-currents)
2. [Dynamical systems and stability](#2-dynamical-systems-and-stability)
3. [Similarity, symmetry, and scale](#3-similarity-symmetry-and-scale)
4. [Optimal control](#4-optimal-control)
5. [Information constraints](#5-information-constraints)
6. [Inverse problems](#6-inverse-problems)
7. [Algebraic topology](#7-algebraic-topology)
8. [Monte Carlo methods](#8-monte-carlo-methods)
9. [Structural causal models](#9-structural-causal-models)
10. [Combinatorial reconstruction](#10-combinatorial-reconstruction)

## 1. Probability conservation and currents

**Useful when:** the same occupancy, average, or endpoint might conceal different temporal processes.

**Abstract idea.** An unchanged distribution can contain continuing directional flow. Accumulation and flow are different quantities.

**First principles.** State probabilities sum to one; incoming probability increases occupancy and outgoing probability decreases it. States and transitions are primitives. Describing transitions with rates determined by the present state additionally assumes a continuous-time Markov model.

**Mathematics.** Let $p_i(t)$ be occupancy probability and $k_{ij}$ the rate from state $i$ to state $j$. Net current and conservation are

$$
J_{ij}=p_i k_{ij}-p_j k_{ji},
\qquad \dot p_i=-\sum_jJ_{ij}.
$$

Stationarity requires $\dot p_i=0$ for each state. Detailed balance requires $J_{ij}=0$ for every pair. For ordinary states even under time reversal, detailed balance expresses equilibrium reversibility; stationarity alone permits circulation.

**Algorithm.**

1. Define observable states and a sufficiently resolved trajectory during an approximately stationary period.
2. Count transitions $N_{ij}$, time in each state $T_i$, and total time $T$.
3. Estimate $\hat p_i=T_i/T$, $\hat k_{ij}=N_{ij}/T_i$, and $\hat J_{ij}=(N_{ij}-N_{ji})/T$ where exposure is sufficient.
4. Quantify uncertainty and sensitivity to state definitions and sampling interval.

**Specific examples.** A constructed three-state ring with clockwise rate $a$ and counterclockwise rate $b$ has uniform stationary occupancy $1/3$ and current $(a-b)/3$. Rates $(a,b)=(2,2)$ and $(3,1)$ per second give the same occupancy and exit rate, but currents $0$ and $2/3$ per second. Time ordering resolves a distinction that occupancy misses.

Battle and colleagues used probability fluxes in observed configuration spaces to detect broken detailed balance in biological motion, including flagellar motion. Frishman and Ronceray developed methods for learning stochastic dynamics from trajectories; the counting algorithm above is an elementary illustration, not a reproduction of their full method.

**Boundary.** Hidden states and unresolved transitions can conceal currents. A finite-interval transition matrix is not automatically a rate matrix. Velocity and other odd variables need the appropriate time-reversal transformation. Quantitative physical entropy production requires additional thermodynamic assumptions.

**Sources:** [Seifert, 2012](https://arxiv.org/abs/1205.4176); [Frishman & Ronceray, 2020](https://doi.org/10.1103/PhysRevX.10.021009); [Battle et al., 2016](https://doi.org/10.1126/science.aac8167).

## 2. Dynamical systems and stability

**Useful when:** the question concerns trajectories, recovery, feedback, switching, or differences hidden by a final state.

**Abstract idea.** Repeated local changes produce global behavior. A small displacement can decay, grow, or change direction.

**First principles.** Choose state variables and a rule for their rate of change. A sufficient state, omitted influences, deterministic versus stochastic dynamics, and timescale are modeling choices. A fixed point produces no change under that rule.

**Mathematics.** For scalar state $x$ and parameter $\mu$, write $\dot x=f(x;\mu)$. At $f(x^*;\mu)=0$, a displacement $\delta=x-x^*$ obeys

$$
\dot\delta\approx f'(x^*)\delta,
\qquad \delta(t)\approx\delta(0)e^{f'(x^*)t}.
$$

Negative derivative implies local decay, positive derivative local growth, and zero derivative leaves the linear test inconclusive. For multiple variables use Jacobian eigenvalues: negative real parts imply local asymptotic stability; any positive real part implies instability; zero real parts require further analysis.

SINDy fits $\dot X\approx\Theta(X)\Xi$, where rows of $X$ are sampled states, $\Theta(X)$ contains candidate functions, and sparse coefficients $\Xi$ select a small candidate equation.

**Algorithm.**

1. Sample trajectories across relevant initial conditions, transients, and parameters.
2. Estimate derivatives with attention to measurement noise.
3. Construct a scientifically plausible candidate-function library and fit sparse coefficients.
4. Integrate the fitted equation and evaluate held-out trajectories, not only derivative fit.
5. Locate fixed points, assess stability, and vary parameters to inspect changes.

**Specific examples.** For the constructed nondimensional model $\dot x=\mu+x-x^3$, at $\mu=0$ the fixed points are $-1,0,1$ with derivatives $-2,+1,-2$. Two stable outcomes can occur at one parameter value, depending on initial state.

The SINDy fluid-flow example illustrated how including transients can reveal dynamics missing from observations confined to an attractor. Work on critical transitions relates slowing recovery to some changes in stability.

**Boundary.** A fixed point is not necessarily thermodynamic equilibrium. Sparse fitting cannot select omitted variables or terms and does not establish a unique governing law. Hysteresis-like loops may reflect delayed response; critical slowing is conditional, not universal.

**Sources:** [Brunton, Proctor, & Kutz, 2016](https://arxiv.org/abs/1509.03580); [Scheffer et al., 2009](https://doi.org/10.1038/nature08227).

## 3. Similarity, symmetry, and scale

**Useful when:** apparently different systems might share a reduced description, or conclusions change with resolution, size, or units.

**Abstract idea.** Remove distinctions that do not affect the chosen behavior, then examine which distinctions reappear when scale changes.

**First principles.** Changing units preserves the physical situation. A symmetry preserves a specified relationship under a transformation. Coarse-graining discards detail and may change the effective equation. These three operations need separate justification.

**Mathematics.** For quantities $q_i$, dimensionless products satisfy

$$
\Pi=\prod_i q_i^{a_i},\qquad Ma=0,
$$

where each column of the dimension matrix $M$ contains a quantity's base-unit exponents. For a translation-invariant observable,

$$
F(x_1+c,x_2+c)=F(x_1,x_2)\ \text{for all }c
\quad\Rightarrow\quad F(x_1,x_2)=G(x_2-x_1).
$$

For independent unbiased steps $\pm\ell$ every $\tau$, $\operatorname{Var}(x_n)=n\ell^2=2Dt$ with $t=n\tau$ and $D=\ell^2/(2\tau)$. The diffusion coefficient summarizes spreading under these assumptions.

**Algorithm.**

1. List variables, units, geometry, boundaries, and the observable to preserve.
2. Compute dimensionless combinations and identify justified symmetries.
3. Replace redundant coordinates with invariant combinations and test the reduced relation.
4. For scale questions, aggregate at several resolutions and re-estimate effective quantities.
5. Compare entire rescaled curves or distributions and their deviations, not only fitted exponents.

**Specific examples.** In a constructed transport case, speed $U$, distance $L$, and diffusivity $D$ give $\mathrm{Pe}=UL/D$, the ratio of diffusion time $L^2/D$ to transport time $L/U$. With $U=10^{-3}$ m/s and $D=10^{-9}$ m²/s, $L=1$ mm gives $\mathrm{Pe}=1000$; $L=1$ μm gives $\mathrm{Pe}=1$. Equal characteristic times do not imply equal measured flux.

Sethna and colleagues discussed crackling-noise profiles of the form $\langle V(t,T)\rangle=T^\alpha F(t/T)$, where $T$ is event duration. Full profile shapes can distinguish models agreeing on exponents. AI Feynman uses structural properties, including dimensional and symmetry information, in symbolic equation discovery.

**Boundary.** Matching dimensionless numbers is insufficient if geometry or mechanisms differ. Collapse does not uniquely identify a microscopic model. Diffusive width growing as $\sqrt t$ describes a distribution, not monotonic individual motion.

**Sources:** [Buckingham, 1914](https://doi.org/10.1103/PhysRev.4.345); [Udrescu & Tegmark, 2020](https://arxiv.org/html/1905.11481); [Sethna, Dahmen, & Myers, 2001](https://arxiv.org/abs/cond-mat/0102091).

## 4. Optimal control

**Useful when:** actions affect both immediate outcomes and future options, or uncertainty changes a preferred policy.

**Abstract idea.** Evaluate an action through its immediate cost and the consequences it makes possible later.

**First principles.** Specify state $s$, action $a$, transition probabilities $P$, cost $c$, horizon $T$, and terminal value. A state sufficient to predict transitions enables recursive evaluation. The objective is a model assumption, not an empirical discovery about what an organism optimizes.

**Mathematics.** The minimum expected remaining cost obeys the Bellman recursion:

$$
V_t(s)=\min_a\left[c(s,a)+\sum_{s'}P(s'\mid s,a)V_{t+1}(s')\right].
$$

A restricted stochastic-control connection uses $dx=(f(x)+B(x)u)\,dt+\sigma(x)\,dW$ and quadratic action cost $u^\top Ru/2$. Here $u$ is control, $W$ Brownian motion, and $R$ a positive-definite cost matrix. When noise and control satisfy

$$
\sigma\sigma^\top=\lambda BR^{-1}B^\top,\quad
V=-\lambda\log\psi,\quad
\psi=\mathbb E_0[e^{-S[\tau]/\lambda}],\quad
u^*=-R^{-1}B^\top\nabla V,
$$

the transformed control equation is linear. $\lambda>0$ sets the cost scale, $\mathbb E_0$ averages uncontrolled paths, and $S[\tau]$ includes state and terminal costs along path $\tau$.

**Algorithm.**

1. Define state, actions, dynamics, costs, horizon, and terminal values.
2. Work backward: calculate each action's immediate plus expected future cost.
3. Retain the minimizing action at each state and time.
4. If the restricted path-integral assumptions hold, sample uncontrolled trajectories, weight by exponential cost, estimate transformed value, and recover control with the appropriate gradient or equivalent estimator.

**Specific examples.** A constructed route A costs $4+100p$ in expectation, with failure probability $p$; route B costs $8$. A is preferred at $p=0.01$ and B at $p=0.20$. Kappen's simulated control examples showed noise-dependent route preferences and timing of commitment between alternatives.

**Boundary.** State, objective, dynamics, and horizon determine the result. Partial observation may require a belief distribution. Path-integral control is conditional on the specified noise and cost structure; it is not a generic recipe for arbitrary dynamics.

**Sources:** [Bellman, 1954](https://doi.org/10.1287/opre.2.3.275); [Kappen, 2005](https://arxiv.org/html/physics/0505066v2).

## 5. Information constraints

**Useful when:** a representation must discard detail while preserving particular predictions or tolerating specified errors.

**Abstract idea.** Compression has meaning relative to the distinctions a task requires.

**First principles.** Specify input $X$, representation $Z$, encoder $q(z\mid x)$, and either distortion $d(x,z)$ or relevance variable $Y$. These criteria define usefulness. The bottleneck factorization $p(x,y,z)=p(x,y)q(z\mid x)$ assumes the encoder accesses $Y$ only through $X$.

**Mathematics.** With logarithms in base two, mutual information is $I(X;Z)=\sum_{x,z}p(x,z)\log_2[p(x,z)/(p(x)p(z))]$. Rate distortion and the information bottleneck respectively solve

$$
R(D)=\min_{q:\,\mathbb E[d(X,Z)]\le D}I(X;Z),
\qquad
\min_q\{I(X;Z)-\beta I(Z;Y)\}.
$$

For bottleneck tradeoff parameter $\beta$, the iterative encoder update is

$$
q(z\mid x)\propto q(z)\,
2^{-\beta D_{\mathrm{KL},2}[p(y\mid x)\|q(y\mid z)]}.
$$

The base-two exponential matches divergence measured in bits.

**Algorithm.**

1. Specify or estimate $p(x,y)$ and initialize $q(z\mid x)$.
2. Compute $q(z)=\sum_xp(x)q(z\mid x)$ and $q(y\mid z)=\sum_xp(x,y)q(z\mid x)/q(z)$ for occupied representations.
3. Update the encoder above and normalize over $z$ for each $x$.
4. Iterate to objective stability; use multiple starts and vary $\beta$.

**Specific examples.** For independent fair bits $C,N$, let $X=(C,N)$ and target $Y=C$. Keeping $C$ retains one input bit and one relevant bit; keeping $N$ retains one input bit and zero relevant bits; keeping both retains two input bits and one relevant bit.

For an independent fair binary source with Hamming distortion, $R(D)=1-H_2(D)$ for $0\le D\le1/2$, and zero for $D\ge1/2$, where $H_2(D)=-D\log_2D-(1-D)\log_2(1-D)$. At $D=0.1$, the asymptotic rate is about $0.531$ bits per symbol. Blahut supplied a computational rate-distortion approach; the information bottleneck formalizes preserving predictive relevance.

**Boundary.** The criterion determines what is discarded. Iteration need not reach a global optimum. An asymptotic rate is not an individual-symbol guarantee, and bits are not automatically physical energy or biological effort.

**Sources:** [Blahut, 1972](https://doi.org/10.1109/TIT.1972.1054855); [Tishby, Pereira, & Bialek, 1999/2000](https://arxiv.org/abs/physics/0004057).

## 6. Inverse problems

**Useful when:** different hidden mechanisms, representations, or objects could produce indistinguishable measurements.

**Abstract idea.** Work backward through the observation process and identify which hidden differences it erases.

**First principles.** Specify unknown object, measurement transformation, and error. A forward model is required. More repetitions of the same measurement can improve precision while preserving structural ambiguity.

**Mathematics.** Ideal attenuation obeys $dI/ds=-\mu(s)I$, so $-\log(I/I_0)=\int_{\mathrm{ray}}\mu(s)\,ds$. Here $\mu$ is attenuation along distance $s$, $I_0$ incident intensity, and $I$ transmitted intensity. Discretization gives

$$
y=Ax+\epsilon,\qquad Av=0\ \Rightarrow\ A(x+v)=Ax.
$$

$x$ contains unknown values, $A$ the measurement geometry, $y$ measurements, and $\epsilon$ error. A null-space change $v$ is invisible to these measurements.

**Algorithm.**

1. Derive or inspect the forward model and identify observationally equivalent objects.
2. Seek additional measurements sensitive to differences in the null space.
3. For basic algebraic reconstruction, initialize $x$ and cycle through nonzero measurement rows $a_i^\top$:

$$
x\leftarrow x+\frac{y_i-a_i^\top x}{\|a_i\|^2}a_i.
$$

4. Use noise-appropriate stopping or regularization; check stability as well as fit.

**Specific examples.** Constructed four-pixel images $X(t)=\begin{pmatrix}t&3-t\\4-t&3+t\end{pmatrix}$ all have row sums $(3,7)$ and column sums $(4,6)$. Nonnegativity allows $0\le t\le3$. Measuring diagonal sum $5$ adds $3+2t=5$, selecting $t=1$. Repeating the original sums cannot do this.

Cormack developed absorption-reconstruction mathematics; Hounsfield described a working transmission-scanning system producing cranial absorption images. Gordon and colleagues developed algebraic reconstruction techniques.

**Boundary.** Uniqueness and stability differ. A unique solution can be noise-sensitive. Regularization adds assumptions such as smoothness, not new observations. A mathematically possible additional measurement still requires a feasible observation process.

**Sources:** [Cormack, 1963](https://doi.org/10.1063/1.1729798); [Gordon, Bender, & Herman, 1970](https://doi.org/10.1016/0022-5193(70)90109-8); [Hounsfield, 1973](https://doi.org/10.1259/0007-1285-46-552-1016).

## 7. Algebraic topology

**Useful when:** connectivity, loops, or higher-dimensional organization may matter beyond exact coordinates or a chosen geometric template.

**Abstract idea.** Describe structural features preserved under certain deformations.

**First principles.** Points, edges, filled triangles, and higher-dimensional elements encode relationships. A closed chain surrounding an unfilled region differs from the boundary of a filled region. Graph cycles alone therefore do not settle the number of holes.

**Mathematics.** Boundary operators satisfy $\partial_{k-1}\partial_k=0$. Homology and its dimension are

$$
H_k=\ker(\partial_k)/\operatorname{im}(\partial_{k+1}),
\qquad \beta_k=\dim H_k.
$$

Closed $k$-chains are compared after treating boundaries of filled $(k+1)$-dimensional elements as trivial. Over a specified coefficient field, $\beta_0$ counts components and $\beta_1$ independent loops. The example below uses arithmetic modulo two.

**Algorithm.**

1. Choose the metric and calculate point distances.
2. Increase an edge-distance threshold $r$; join points with distance at most $r$.
3. Fill each clique with its corresponding simplex, forming a Vietoris-Rips filtration.
4. Order simplices by entry time, construct boundary matrices, and reduce modulo two.
5. Record feature intervals $[\text{birth},\text{death})$ and assess sensitivity to metric and sampling.

**Specific examples.** For the constructed unit-square corners, $r<1$ gives four components; $1\le r<\sqrt2$ gives one component and one loop; $r\ge\sqrt2$ adds diagonals and filled triangles, killing the loop. Its interval is $[1,\sqrt2)$ under this edge-distance convention.

Hiraoka and colleagues characterized ring hierarchies in simulated atomic configurations of disordered materials. Gardner and colleagues used persistent cohomology to identify toroidal structure in grid-cell population activity.

**Boundary.** Threshold conventions matter: edge distance and ball radius are not interchangeable. Persistence depends on metric, sampling, and construction. A persistent feature does not by itself identify a generating mechanism or biological significance.

**Sources:** [Edelsbrunner, Letscher, & Zomorodian, 2002](https://doi.org/10.1007/s00454-002-2885-2); [Hiraoka et al., 2016](https://arxiv.org/html/1501.03611); [Gardner et al., 2022](https://www.nature.com/articles/s41586-021-04268-7).

## 8. Monte Carlo methods

**Useful when:** a quantity requires averaging over too many possibilities for direct enumeration, and computational effort can be redistributed through sampling.

**Abstract idea.** Estimate a large calculation by sampling contributions and correcting their unequal probabilities.

**First principles.** Specify the target integral, sampling distribution, estimator, and uncertainty. The sampling distribution is a computational choice, not a change to the target quantity. Support coverage and finite variance are substantive conditions.

**Mathematics.** For $I=\int f(x)\,dx$, choose a normalized density $q(x)>0$ wherever $f$ contributes. For independent draws $X_i\sim q$,

$$
I=\mathbb E_q[f(X)/q(X)],\qquad
\hat I_N=\frac1N\sum_{i=1}^N\frac{f(X_i)}{q(X_i)},
$$

$$
\operatorname{Var}(\hat I_N)=\frac1N
\left[\int\frac{f(x)^2}{q(x)}\,dx-I^2\right].
$$

With finite variance the standard deviation scales as $N^{-1/2}$; the variance constant depends on $q$.

**Algorithm.**

1. Express the target as an integral and choose $q$ with adequate support.
2. Sample, calculate contributions $w_i=f(X_i)/q(X_i)$, and average.
3. Estimate uncertainty and inspect whether extreme weights dominate.
4. Improve the proposal when useful while preserving the appropriate weighting and uncertainty calculation.

**Specific examples.** For the constructed integral $\int_0^1x^2dx=1/3$, uniform sampling has estimator variance $4/(45N)$. Sampling $q(x)=2x$ gives contribution $x/2$ and variance $1/(72N)$, a 6.4-fold reduction.

Dürr and colleagues used lattice-QCD computations, with Hybrid Monte Carlo variants, to calculate the light-hadron spectrum. Three hadronic quantities fixed parameters and scale; the remaining spectrum provided predictions agreeing with measurements. These samples are correlated, unlike the independent teaching estimator.

**Boundary.** The convergence rate does not guarantee affordable computation. Rare events, poor proposals, and correlations can make sampling inefficient. Correlated trajectories require a different variance calculation. Unnormalized proposals or self-normalized estimators also require their own derivation.

**Sources:** [Metropolis & Ulam, 1949](https://doi.org/10.1080/01621459.1949.10483310); [Lepage, 2021](https://arxiv.org/html/2009.05112); [Dürr et al., 2008, spectrum](https://arxiv.org/abs/0906.3599); [Dürr et al., 2008, methods](https://arxiv.org/html/0802.2706).

## 9. Structural causal models

**Useful when:** the scientific question concerns setting, disabling, or changing a mechanism, and observation may differ from intervention.

**Abstract idea.** Replace a generating mechanism and calculate the consequences of the modified system.

**First principles.** Observation records outcomes; conditioning selects cases; intervention changes how a variable is produced. Mechanism modularity, the causal structure, and which other mechanisms remain invariant are assumptions.

**Mathematics.** Write $X_i=f_i(\mathrm{parents}_i,U_i)$, where $U_i$ represents additional influences. The intervention $\operatorname{do}(X=x)$ replaces the assignment for $X$ with a constant. For the simple sufficient-adjustment graph $U\to X$, $U\to Y$, $X\to Y$,

$$
p(y\mid\operatorname{do}(X=x))=\sum_u p(y\mid x,u)p(u),
\qquad
p(y\mid X=x)=\sum_u p(y\mid x,u)p(u\mid x).
$$

The averages use different distributions of $U$. Using the first expression from data requires the graph's identification assumptions and relevant observations of $U$.

**Algorithm.**

1. Specify intervention, outcome, target population, and assumed causal relationships.
2. Determine whether available variables identify the effect; adjustment is only one possible case.
3. Check overlap for the needed comparisons and estimate outcomes within adjustment groups.
4. Average both intervention conditions over the same target-population distribution and compare.
5. Examine sensitivity to unmeasured causes, unsuitable adjustment, and changes to other mechanisms.

**Specific examples.** Constructed workload $U$ is a fair binary variable; fan $X$ operates with probability $0.8$ at high workload and $0.2$ at low workload. Temperature $Y=20+10U-4X$ gives observed means $24$ with fan on and $22$ off, but intervention means $21$ on and $25$ off. Association is $+2$ degrees while the intervention effect is $-4$.

Sachs and colleagues combined single-cell measurements and molecular perturbations to infer signaling relationships. Inhibiting Erk1 reduced Akt phosphorylation, supporting an inferred influence that the authors allowed could be indirect.

**Boundary.** A graph does not prove its own correctness. Hidden causes, absent overlap, inappropriate adjustment, or interventions changing additional mechanisms can invalidate the calculation. Mechanism replacement must correspond to the intervention being studied.

**Sources:** [Pearl, 1995](https://doi.org/10.1093/biomet/82.4.669); [Pearl, 2009](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf); [Sachs et al., 2005](https://doi.org/10.1126/science.1105809).

## 10. Combinatorial reconstruction

**Useful when:** global order or structure must be reconstructed from local fragments, overlaps, or compatibility rules.

**Abstract idea.** Choose a representation that makes local constraints computationally usable while exposing global ambiguity.

**First principles.** Define fragments, allowed adjacency, multiplicity, and valid reconstruction. What counts as a vertex, an edge, and a traversal determines the mathematical problem.

**Mathematics.** A $k$-mer is a length-$k$ substring. Represent it as a directed edge from its length-$(k-1)$ prefix to its suffix. For an exact multiset of occurrences, a reconstruction uses every edge occurrence once, an Eulerian trail. A nonclosed trail requires

$$
\deg^+(v)-\deg^-(v)=
\begin{cases}
1,&v\text{ is the start},\\
-1,&v\text{ is the end},\\
0,&\text{otherwise},
\end{cases}
$$

and weak connectivity of the edge-bearing graph, meaning connectivity when edge directions are ignored. A closed trail has balanced degrees throughout and the same connectivity condition. $\deg^+$ and $\deg^-$ count outgoing and incoming edge occurrences.

**Algorithm.**

1. Convert each error-free $k$-mer occurrence into an edge, preserving multiplicities.
2. Check degree/connectivity conditions and select a valid starting vertex.
3. Follow unused outgoing edges, pushing visited vertices onto a stack.
4. At a vertex with no unused outgoing edge, pop it into the output.
5. Continue until the stack empties, reverse output, and spell the sequence by appending one character per traversed edge.
6. Check all edge occurrences were used; distinguish a compatible reconstruction from a unique one.

**Specific examples.** Constructed fragments ATG twice, TGA twice, and GAT once admit the sequence ATGATGA. In contrast, TACAGAT and TAGACAT have the same multiset of 2-mers, so those local constraints do not determine the original order.

Pevzner and colleagues developed Eulerian fragment assembly. Velvet combined de Bruijn graph representations with error removal and repeat handling, including assembly from actual Solexa reads.

**Boundary.** Efficient traversal does not prove uniqueness. Actual read counts reflect sequencing coverage as well as genomic repetition. Errors, missing fragments, strand orientation, and repeats make practical assembly more complex than the complete, error-free multiset problem.

**Sources:** [Pevzner, Tang, & Waterman, 2001](https://doi.org/10.1073/pnas.171285098); [Zerbino & Birney, 2008](https://doi.org/10.1101/gr.074492.107).
