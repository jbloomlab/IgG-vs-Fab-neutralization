import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # IgG versus Fab virus neutralization

    Analysis by [Jesse Bloom](https://jbloomlab.org/) of viral neutralization by IgG and Fab accounting for the effects of avidity and ligand depletion.
    The quantitative model is described first, then at bottom is an interactive plot implementing the model, followed by comparison to real data.

    ## Fab binding
    Let the binding affinity of the Fab have dissociation constant $K_D$.
    There are two possible states, unbound ($U$) and bound ($B$).
    The Boltzmann weights for these two states as a function of the molar concentration $c$ of Fab are $w_U\left(c\right) = 1$ and $w_B\left(c\right) = \frac{c}{K_D}$.

    So the probability of the unbound state as a function of $c$ is
    $$p^{\rm{Fab}}_u\left(c\right) = \frac{w_U\left(c\right)}{w_U\left(c\right) + w_B\left(c\right)} = \frac{1}{1 + c/K_D}.$$

    This two-state partition-function formulation for monovalent binding follows classic multivalency treatments ([Perelson & DeLisi, 1980](https://www.sciencedirect.com/science/article/abs/pii/0025556480900176); [Hlavacek et al., 1999](https://pubmed.ncbi.nlm.nih.gov/10354429/)).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## IgG binding
    For the IgG, we will assume each arm of the bivalent IgG has the same monovalent affinity for the viral antigen as the Fab described above.
    However, once the first arm binds, the effective concentration $c_{\rm{eff}}$ of the second arm is set by the density/spacing of viral antigens and the reach of the antibody.
    Here we do not consider those factors (antigen density, antibody reach, etc) separately, but just collapse them into the single effective concentration of the second arm after the first has bound, $c_{\rm{eff}}$.
    The definition of an effective local concentration for the second arm, set by geometry/linker statistics rather than bulk concentration mirrors prior work ([Einav et al., 2019](https://www.cell.com/cell-systems/pdf/S2405-4712%2819%2930315-1.pdf); [Mammen, Choi, & Whitesides, 1998](https://pubmed.ncbi.nlm.nih.gov/29711117/); [Fasting et al., 2012](https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201201114)).
    In realistic scenarios, if bivalent binding is possible then $c_{\rm{eff}} \gg c$ since the effective concentration of the second Fab arm in proximity to the viral antigen after the first arm has bound is much higher than the overall IgG concentration (note that concentrations should be in *molar* units rather than ng/ml in order to allow the same concentration scale to be used for Fab and IgG, since they have different molecular weights).

    There are now three possible states, unbound ($U$), a single Fab arm bound ($B_1$), and both Fab arms bound ($B_2$).
    The Boltzmann weights for these three states as a function of the molecular concentration of IgG are $w_U\left(c\right) = 1$, $w_{B_1}\left(c\right) = \frac{c}{K_D}$, and $w_{B_2}\left(c\right) = \frac{c}{K_D}\times\frac{ c_{\rm{eff}}}{K_D}$.
    Further, note that state $B_1$ has a multiplicity of two since either of the Fab arms can bind ([Perelson & DeLisi, 1980](https://www.sciencedirect.com/science/article/abs/pii/0025556480900176)).

    So the probability of the unbound state as a function of $c$ is (accounting for the multiplicity of two for $B_1$)
    $$p_u^{\rm{IgG}}\left(c\right) = \frac{w_U\left(c\right)}{w_U\left(c\right) + 2 w_{B_1}\left(c\right) + w_{B_2}\left(c\right)} = \frac{1}{1 + 2 \frac{c}{K_D} + \frac{c}{K_D} \frac{c_{\rm{eff}}}{K_D}} = \frac{1}{1 + \frac{c}{K_D}\left(2 + \frac{c_{\rm{eff}}}{K_D}\right)}.$$

    Note that the effective dissociation constant of the IgG is $K_D^{\rm{IgG}} = K_D / \left(2 + \frac{c_{\rm{eff}}}{K_D}\right)$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Assumption: binding affinity equals neutralization potency
    In the rest of this document, we assume that binding affinity equals neutralizaton potency, such that the neutralization IC50 of the Fab is equivalent to $K_D$.
    In other words, we equate fraction infectivity with fraction of viral epitopes ($p_u$); as described immediately below deviations can occur under multi-hit models.

    Specifically, how fraction bound (binding affinity) relates to neutralization potency depends on how many antibodies must bind to a virion in order to neutralize it.
    The quantitative relationship between binding affinity and neutralization potency as well as its impact on the neutralization curve slope can be modeled under assumptions about the number of spikes per virions and the number that must be bound to neutralize (see [Magnus et al, 2013](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1002900), [Brandenburg et al, 2017](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1006313), [Pierson et al., 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC2656919/); [Klasse, 2014](https://pubmed.ncbi.nlm.nih.gov/27099867/), [Yang et al, 2005](https://pmc.ncbi.nlm.nih.gov/articles/PMC1075697)).

    Here we are going to **ignore** this issue for now, and just conflate neutralization IC50 with Fab $K_D$.
    This is a quantitative simplification, but should not affect the main qualitative trends--and has the advantage of not requiring us to estimate difficult to determine quantities such as how many spikes there are per virion and what fraction of them must be bound for neutralization.
    Note that in the limiting case where this is just one spike per virion and binding one site on it is sufficient for neutralization, then ignoring this issue has no effect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Estimating $c_{\rm{eff}}$ from the IgG versus Fab IC50
    We can estimate $c_{\rm{eff}}$ (the parameter that describes the extent of avidity from bivalent binding) from the IC50 (or midpoint on the neutralization curve) of the IgG versus Fab.
    In particular, let $m_{\rm{Fab}}$ and $m_{\rm{IgG}}$ be the molar concentrations at the midpoint (IC50) of the Fab versus IgG neutralization curves, respectively.
    Then $K_D = m_{\rm{Fab}}$ and $1/2 = \frac{1}{1 + \frac{m_{\rm{IgG}}}{m_{\rm{Fab}}}\left(2 + \frac{c_{\rm{eff}}}{m_{\rm{Fab}}}\right)}.$
    Solving for $c_{\rm{eff}}$ yields
    $c_{\rm{eff}} = m_{\rm{Fab}}\left(\frac{m_{\rm{Fab}}}{m_{\rm{IgG}}} - 2\right).$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Impact of mutation(s)
    Consider one or more mutations that cause a fold change in Fab IC50 of $f_{\rm{mut}}$.
    For instance, a mutation that increases the Fab IC50 by 10-fold would have $f_{\rm{mut}} = 10$.
    Note that mutations that cause a fixed change in the free energy of binding are expected to cause the same fold change in Fab IC50 in any genetic background.

    In the presence of these mutation(s), the fraction of Fab not neutralized becomes
    $$p_u^{\rm{Fab}}\left(c\right) = \frac{1}{1 + \frac{c}{f_{\rm{mut}} \times K_D}}$$
    and the fraction of IgG not neutralized becomes
    $$p_u^{\rm{IgG}}\left(c\right) = \frac{1}{1 + \frac{c}{f_{\rm{mut}} \times K_D} + \left(2 + \frac{c_{\rm{eff}}}{f_{\rm{mut}} \times K_D}\right)}.$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Complication: accounting for ligand depletion
    Everything above is written in terms of the antibody (Fab or IgG) concentration $c$.
    In fact, in these equations refer to the _free_ concentration of antibody.
    But when the concentration of viral antigen is comparable to or exceeds the dissociation constant of the antibody ($K_D$ for the Fab and $K_D^{\rm{IgG}}$ for the IgG), there can be "ligand depletion," which is the term we use here for when a large fraction of the antibody is bound to the viral antigen.
    When this occurs, much of the antibody gets "soaked up" by binding to viral antigen, and so the actual concentration of free antibody in the neutralization assay represented by $c$ in the above equations is appreciably less than the total concentration added to the reaction.
    This phenomenon is nicely described in detail by [Jarmoskaite et al (2020)](https://doi.org/10.7554/eLife.57264), who refer to it as the "titration regime."

    To quantatively deal with this, we need to define some additional variables.
    Let $c_{\rm{total}}$ be the total antibody concentration added the assay volume, let $c_{\rm{free}}$ be the concentration of antibody that is not bound to viral antigen (free), and let $c_{\rm{bound}}$ be the concentration of antibody that is bound to viral antigen.
    Also, let $v_{\rm{total}}$ be the total concentration of viral antigen (quantified in terms of number of the relevant epitope per unit volume), let $v_{\rm{free}}$ be the concentration of free viral antigen (not bound by antibody), and note that concentration of bound viral antigen is $c_{\rm{bound}}$.
    We have the following equations:
    $c_{\rm{total}} = c_{\rm{free}} + c_{\rm{bound}}$ (mass balance for the antibody),
    $v_{\rm{total}} = v_{\rm{free}} + c_{\rm{bound}}$ (mass balance for the viral antigen), and $c_{\rm{bound}} K_D^{\rm{effective}} = v_{\rm{free}} c_{\rm{free}}$ (there is an equilibrium with respect to the free antibody and antigen concentration). Note that for the Fab, $K_D^{\rm{effective}} = K_D$ and for the IgG, $K_D^{\rm{effective}} = K_D^{\rm{IgG}}$.
    Solving this system of three equations yields ([Jarmoskaite et al (2020)](https://doi.org/10.7554/eLife.57264))
    $$c_{\rm{bound}} = \frac{c_{\rm{total}} + v_{\rm{total}} + K_D^{\rm{effective}} - \sqrt{\left(c_{\rm{total}} + v_{\rm{total}} + K_D^{\rm{effective}}\right)^2 - 4 c_{\rm{total}} v_{\rm{total}}}}{2}$$
    and so
    $$c_{\rm{free}} = c_{\rm{total}} - c_{\rm{bound}} = \frac{c_{\rm{total}} - v_{\rm{total}} - K_D^{\rm{effective}} + \sqrt{\left(c_{\rm{total}} + v_{\rm{total}} + K_D^{\rm{effective}}\right)^2 - 4 c_{\rm{total}} v_{\rm{total}}}}{2}.$$

    Note that in the limit where the viral antigen concentration is limiting and so we are outside the ligand depletion regime (eg, $v_{\rm{total}} \ll K_D^{\rm{effective}}$), then we just have $c_{\rm{free}} \approx c_{\rm{total}}$.
    However, when the viral antigen concentration is comparable or greater to $K_D^{\rm{effective}}$, then it is important to substitute $c_{\rm{free}}$ for $c$ in all of the equations above.

    We can also calculate the actual observed IC50s accounting for ligand depletion.
    The IC50 under our assumption above that this is when half of viral epitopes are bound) occurs when $\frac{1}{2} = \frac{c_{\rm{bound}}}{v_{\rm{total}}}.$
    It turns out that this can be neatly solved to determine the actual observed IC50 (accounting for ligand depletion) is
    $$c_{\rm{{IC50,observed}}}=K_D^{\rm{effective}} + \frac{v_{\rm{total}}}{2},$$
    whereas the ideal IC50 if there is no ligand depletion (when $v_{\rm{total}} \ll K_D^{\rm{effective}}$) is just
    $$c_{\rm{IC50,ideal}} = K_D^{\rm{effective}}.$$

    The floor on the measurable IC50 (eg, the lowest value that can be measured) is $\sim v_{\rm{total}} / 2$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Some realistic parameter estimates

    We ballpark (these are rough estimates) realistic parameter values for Nirsevimab from our experiments.
    For the Fab IC50, which is represented by $m_{\rm{Fab}}$ or $K_D$ in the above equations:
      - subgroup A (Long) strain: $K_D \sim 0.01$ nM
      - subgroup B (B1) strain: $K_D \sim 1$ nM

    We also need to estimate $c_{\rm{eff}}$; however, doing that is complicated by the fact that at least for subgroup A, the IgG neutralization assays are likely in the ligand depletion range (what [Jarmoskaite et al (2020)](https://elifesciences.org/articles/57264) call the "titration regime") where the IgG IC50 ($m_{\rm{IgG}}$) cannot be measured accurately since the concentration of the viral antigen protein likely is comparable or greater to the true IgG IC50.
    So we will use neutralization measurements against the subgroup B (B1) strain as any IgG ligand depletion should be less here due to the lower potency, and we assume that the actual avidity (potential for bivalent binding) captured in $c_{\rm{eff}}$ should not be strain dependent.
    Against this strain, we have $m_{\rm{IgG}} \sim 0.01$ nM and $m_{\rm{Fab}} \sim 1$ nM.
    So this gives $c_{\rm{eff}} \sim 100$ nM.
    However, there is probably still ligand depletion in the measurement of $m_{\rm{IgG}}$ since the subtype B IgG neutralization is just as good as subtype A, so we will add another factor of to and use $c_{\rm{eff}} \sim 1000$ nM.

    The hardest parameter to estimate is the number of viral epitopes $v_{\rm{total}}$ which determines if there is ligand depletion.
    Roughly, we might estimate $10^6$ infectious particles per ml, with a $10^2$ non-infectious particles for each infectious one, $10^2$ epitopes per particle.
    In that case, we have $10^{13}$ epitopes / liter, which gives $v_{\rm{total}} \sim 0.01$ nM.
    Note that this is very much a ballpark estimate, and could vary by an order of magnitude or more in either direction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Visualizing IgG and Fab neutralization how it is affected by mutations

    We now plot interactive visualizations initialized with the ballpark-realistic parameter values above for the subgroup A strain of how nirsevimab neutralization differs between the Fab and IgG and how this is impacted by mutations.
    In the interactive chart below, you can use the sliders to adjust the Fab affinity ($K_D$), the avidity ($c_{\rm{eff}}$), the effect of the viral mutation(s), and the viral epitope concentration.
    As you do so, you can see how the neutralization curves and IC50s change.
    Note for the IC50s it shows both the actual observed IC50 (accounting for legend depletion) as well as what would be the ideal IC50 in the absence of any ligand depletion.
    """)
    return


@app.cell
def _():
    import math

    import altair as alt

    import marimo as mo

    import numpy

    import pandas as pd

    # --- Data over concentration (nM) on a log grid ---
    concentrations = numpy.logspace(-4, 3, 400)   # 0.001 nM to 1000 nM
    df = pd.DataFrame({"c": concentrations})

    # --- Interactive parameters ---
    log10_KD = alt.param(
        name="log10_KD",
        value=-2,
        bind=alt.binding_range(
            min=-3,
            max=3,
            step=0.1,
            name="Fab neutralization potency: log10 KD (nM)",
        ),
    )

    log10_c_eff = alt.param(
        name="log10_c_eff",
        value=3,
        bind=alt.binding_range(
            min=-2,
            max=5,
            step=0.1,
            name="avidity for IgG: log10 c_eff (nM)",
        ),
    )

    log10_f_mut = alt.param(
        name="log10_f_mut",
        value=1.3,
        bind=alt.binding_range(
            min=-1,
            max=3,
            step=0.1,
            name="viral mutation impact on Fab neutralization (fold change): log10 f_mut",
        )
    )

    log10_v_total = alt.param(
        name="log10_v_total",
        value=-2,
        bind=alt.binding_range(
            min=-5,
            max=0,
            step=0.1,
            name="viral epitope concentration (nM): log10 v_total",
        ),
    )

    # formatting for different antibody types
    line_format = {
        "Fab": ("#1f77b4", [1, 0]),
        "Fab mutant": ("#6baed6", [2, 2]),
        "IgG": ("#ff7f0e", [1, 0]),
        "IgG mutant": ("#fdae6b", [2, 2]),
    }

    # Build the base chart
    chart_base = (
        alt.Chart(df)
        .add_params(log10_KD, log10_c_eff, log10_f_mut, log10_v_total)
        .transform_calculate(
            # first get logged parameters to data fields that can be used
            KD="pow(10, log10_KD)",
            c_eff="pow(10, log10_c_eff)",
            f_mut="pow(10, log10_f_mut)",
            v_total="pow(10, log10_v_total)",
            # Now get the KD effective for antibody-virus pairs
            Fab=alt.datum.KD,
            **{"Fab mutant": alt.datum.KD * alt.datum.f_mut},
            IgG=alt.datum.KD / (2 + alt.datum.c_eff / alt.datum.KD),
            **{"IgG mutant": alt.datum["Fab mutant"] / (2 + alt.datum.c_eff / alt.datum["Fab mutant"])},
        )
        .transform_fold(
            ["Fab", "Fab mutant", "IgG", "IgG mutant"],
            ["antibody type", "KD_eff"],
        )
        .transform_calculate(
            # calculate free concentrations
            c_free=(
                (alt.datum.c - alt.datum.v_total - alt.datum.KD_eff)
                + alt.expr.sqrt(
                    (alt.datum.c + alt.datum.v_total + alt.datum.KD_eff)**2
                    - 4 * alt.datum.c * alt.datum.v_total
                )
            ) / 2.0,
            # calculate fractions unbound for mutated and unmutated Fab and IgG
            fraction_infectivity=1 / (1 + alt.datum.c_free / alt.datum.KD_eff),
        )
    )

    # build chart showing IC50s
    ic50_chart = (
        chart_base
        .transform_aggregate(
            ideal="mean(KD_eff)",
            mean_v_total="mean(v_total)",
            groupby=["antibody type"],
        )
        .transform_calculate(
            observed=alt.datum.ideal + alt.datum.mean_v_total / 2,
        )
        .transform_fold(
            ["ideal", "observed"],
            ["IC50 type", "IC50"],
        )
        .encode(
            alt.X("antibody type:N"),
            alt.Y(
                "IC50:Q",
                scale=alt.Scale(type="log", nice=False, padding=10),
                title="IC50 (nM)"
            ),
            alt.Fill(
                "antibody type:N",
                scale=alt.Scale(
                    domain=line_format.keys(),
                    range=[tup[0] for tup in line_format.values()],
                ),
                legend=None,
            ),
            alt.Shape("IC50 type:N", legend=alt.Legend(symbolSize=170)),
            tooltip=[
                "antibody type:N",
                alt.Tooltip("IC50:Q", title="IC50 (nM)", format=".2g"),
                "IC50 type:N",
            ],
        )
        .mark_point(size=170, stroke="black", strokeWidth=1, opacity=0.75)
        .properties(height=250, width=130)
    )

    # Build the neutralization chart
    neut_chart = (
        chart_base
        .mark_line(size=5)
        .encode(
            alt.X(
                "c",
                title="antibody concentration (nM)",
                scale=alt.Scale(type="log"),
            ),
            alt.Y("fraction_infectivity:Q", title="fraction infectivity"),
            alt.Color(
                "antibody type:N",
                scale=alt.Scale(
                    domain=line_format.keys(),
                    range=[tup[0] for tup in line_format.values()],
                ),
                legend=alt.Legend(
                    orient="bottom",
                   titleOrient="left",
                    symbolStrokeWidth=5,
                    symbolSize=700,
                ),
            ),
            alt.StrokeDash(
                "antibody type:N",
                scale=alt.Scale(
                    domain=line_format.keys(),
                    range=[tup[1] for tup in line_format.values()],
                ),
            ),
            tooltip=[
                alt.Tooltip("c", title="concentration (nM)", format=".2g"),
                alt.Tooltip("fraction_infectivity:Q", title="fraction infectivity", format=".2g"),
                alt.Tooltip("antibody type:N"),
                alt.Tooltip("c_free:Q", title="free concentration (nM)", format=".2g"),
            ],
        )
        .properties(width=600, height=320)
    )

    # chart showing floor on measurable IC
    neut_floor = (
        alt.Chart()
        .add_params(log10_v_total)
        .transform_calculate(floor_IC50="pow(10, log10_v_total) / 2")
        .mark_rule(strokeDash=[8, 8], color="gray", size=4, opacity=0.5)
        .encode(alt.X("floor_IC50:Q"))
    )

    # floor on measurable IC50
    ic50_floor = (
        alt.Chart()
        .add_params(log10_v_total)
        .transform_calculate(IC50="pow(10, log10_v_total) / 2")
        .mark_rule(strokeDash=[8, 8], color="gray", size=4, opacity=0.5)
        .encode(alt.Y("IC50:Q"))
    )

    # add a subtitle with hyperlink
    hyperlink_subtitle = (
        alt.Chart(
            pd.DataFrame([{
                "text":
                    "https://jbloomlab.github.io/IgG-vs-Fab-neutralization",
                "url": "https://jbloomlab.github.io/IgG-vs-Fab-neutralization",
            }])
        )
          .mark_text(baseline="bottom", align="left", size=16)
          .encode(
              text="text:N",
              href="url:N",
              color=alt.value("#1a0dab"),
          )
          .properties(height=20)
    )

    # combine charts
    chart = (
        alt.vconcat(
            hyperlink_subtitle,
            ((neut_chart + neut_floor) | (ic50_chart + ic50_floor)),
            spacing=5,
        )
        .resolve_scale(
            color="independent", strokeDash="independent", shape="independent"
        )
        .properties(
            title=alt.TitleParams(
                "IgG versus Fab neutralization",
                subtitle=[
                    "Left plot shows observed neutralization curves against virus and virus mutant by IgG and Fab.",
                    "Right plot shows the observed IC50s, as well as ideal IC50s if there was no ligand depletion.",
                    "Dashed gray line on both plots is floor on observed IC50 due to ligand depletion.",
                    "Adjust Fab potency, IgG avidity, mutation effect, and viral epitope concentration using options at bottom.",
                ],
                fontSize=24,
                subtitleFontSize=16,
                offset=2,
                dx=70
            )
        )
        .configure_axis(titleFontSize=22, labelFontSize=18, grid=False)
        .configure_legend(titleFontSize=22, labelFontSize=22)
    )

    chart.save("chart.html")

    chart
    return mo, numpy, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Now plot real RSV F neutralization data
    These are data from pseudovirus neutralization assays run by Cassie and Teagan with the Long (subtype A) or B1 (subtype B) F proteins:
    """)
    return


@app.cell
def _(pd):
    import neutcurve

    # read all the data
    real_data = pd.read_csv("actual_RSV-F_data.csv")

    # get just the comparisons to plot here in correct format
    data_to_plot = (
        real_data
        .query("date in ['2025-08-28', '2025-10-02']")
        .assign(
            antibody=lambda x: x["serum"].str.split().str[0],
            antibody_type=lambda x: x["serum"].str.split().str[1],
            strain=lambda x: x["virus"].str.split().str[1],
            subtype=lambda x: x["strain"].map({"Long": "A", "B1": "B"}),
            mutant=lambda x: x["virus"].str.split().str[-1].map(
                lambda m: "unmutated" if m == "WT" else m
            ),
            line_type=lambda x: x["antibody_type"] + " vs " + x["mutant"].map(
                lambda m: "mutant" if m != "unmutated" else "unmutated"
            )
        )
        .query("antibody == 'Nirsevimab'")
        .query("mutant in ['unmutated', 'K68Q', 'K201S', 'N201S']")
        .assign(
            comparison=lambda x: x.apply(
                lambda r: (
                    (["K68Q", "K201S"] if r["subtype"] == "A" else ["K68Q", "N201S"])
                    if r["mutant"] =="unmutated"
                    else [r["mutant"]]
                ),
                axis=1,
            )
        )
        .explode("comparison")
        .assign(facet_type=lambda x: "subtype " + x["subtype"] + " vs " + x["comparison"]) 
    )

    # make the plots
    fits_to_plot = neutcurve.CurveFits(
        data_to_plot, serum_col="line_type", virus_col="facet_type"
    )

    lines = ["IgG vs unmutated", "IgG vs mutant", "Fab vs unmutated", "Fab vs mutant"]
    line_color_markers = {
        "Fab vs unmutated": ("#1f77b4", "o"),
        "Fab vs mutant": ("#6baed6", "^"),
        "IgG vs unmutated": ("#ff7f0e", "o"),
        "IgG vs mutant": ("#fdae6b", "^"),
    }

    data_fig, data_axes = fits_to_plot.plotViruses(
        ncol=2,
        viruses=["subtype A vs K68Q", "subtype A vs K201S", "subtype B vs K68Q", "subtype B vs N201S"],
        sera=lines,
        serum_to_color_marker=line_color_markers,
        legendfontsize=15,
        labelsize=15,
        titlesize=15,
        markersize=7,
        linewidth=1.5,
        xlabel="antibody concentration (nM)",
        ylabel="fraction viral infectivity",
    )

    # Postprocess: make mutant lines dashed
    mutant_colors = [v[0] for k, v in line_color_markers.items() if "mutant" in k]
    for _ax in data_axes.flat:
        for _line in _ax.get_lines(): 
            if (_line.get_color() in mutant_colors) and (_line.get_label() == "fit"):
                _line.set_linestyle("--")
                _line.set_dashes([2, 2])  # explicitly set dash pattern
    for _legend in data_fig.legends:
        for _handle, _text in zip(_legend.legend_handles, _legend.get_texts()):
            if "mutant" in _text.get_text():
                _handle.set_linestyle("--")
                _handle.set_dashes([2, 2])

    data_fig.suptitle("actual RSV F pseudovirus neutralization data", fontsize=16, fontweight="bold", x=0.55, y=1.03)

    data_fig
    return data_to_plot, line_color_markers, lines, mutant_colors, neutcurve


@app.cell
def _(mo):
    mo.md(r"""
    ## Plot modeled data in same format as simulated data
    Plot the simulated data in the same way as the real data.
    """)
    return


@app.cell
def _(
    data_to_plot,
    line_color_markers,
    lines,
    mutant_colors,
    neutcurve,
    numpy,
    pd,
):
    # Extract actual concentrations used in experiments for IgG and Fab
    igg_conc = sorted(data_to_plot.query("antibody_type == 'IgG'")["concentration"].unique())
    fab_conc = sorted(data_to_plot.query("antibody_type == 'Fab'")["concentration"].unique())

    # Define small shifts to prevent overlap (multiplicative factors)
    shift_factors = {
        "Fab vs unmutated": 0.97,
        "Fab vs mutant": 1.03,
        "IgG vs unmutated": 0.95,
        "IgG vs mutant": 1.05,
    }

    def simulate_neut_data(KD, c_eff=1000, f_mut=20, v_total=0.01):
        """Simulate neutralization data for Fab and IgG against unmutated and mutant virus."""
        data = []
        for antibody_type, is_igg in [("Fab", False), ("IgG", True)]:
            # Use appropriate concentration range for antibody type
            concentrations = numpy.array(igg_conc if is_igg else fab_conc)

            for mutant_status, fold_change in [("unmutated", 1), ("mutant", f_mut)]:
                line_type = f"{antibody_type} vs {mutant_status}"

                # Apply shift to prevent overlap
                shifted_conc = concentrations * shift_factors[line_type]

                # Calculate effective KD
                KD_eff = KD * fold_change
                if is_igg:
                    KD_eff = KD_eff / (2 + c_eff / KD_eff)

                # Calculate free concentration accounting for ligand depletion
                c_free = (
                    (shifted_conc - v_total - KD_eff) +
                    numpy.sqrt((shifted_conc + v_total + KD_eff)**2 - 4 * shifted_conc * v_total)
                ) / 2

                # Calculate fraction infectivity
                fraction_infectivity = 1 / (1 + c_free / KD_eff)

                data.extend([
                    {
                        "concentration": c,
                        "fraction infectivity": fi,
                        "line_type": line_type,
                        "facet_type": f"KD={KD} nM vs mutation",
                    }
                    for c, fi in zip(shifted_conc, fraction_infectivity)
                ])

        return pd.DataFrame(data)

    # Generate data for two KD values
    sim_data = pd.concat([
        simulate_neut_data(KD=0.01).assign(facet_type="strain bound w high affinity"),
        simulate_neut_data(KD=1.0).assign(facet_type="strain bound w low affinity"),
    ]).assign(replicate=1)

    fits_to_sim = neutcurve.CurveFits(
        sim_data, serum_col="line_type", virus_col="facet_type"
    )

    sim_fig, sim_axes = fits_to_sim.plotViruses(
        ncol=1,
        sera=lines,
        serum_to_color_marker=line_color_markers,
        legendfontsize=15,
        labelsize=15,
        titlesize=15,
        markersize=7,
        linewidth=1.5,
        xlabel="antibody concentration (nM)",
        ylabel="fraction viral infectivity",
        yticklocs=[0, 0.5, 1],
    )

    # Postprocess: make mutant lines dashed
    for _ax in sim_axes.flat:
        for _line in _ax.get_lines(): 
            if (_line.get_color() in mutant_colors) and (_line.get_label() == "fit"):
                _line.set_linestyle("--")
                _line.set_dashes([2, 2])  # explicitly set dash pattern
    for _legend in sim_fig.legends:
        for _handle, _text in zip(_legend.legend_handles, _legend.get_texts()):
            if "mutant" in _text.get_text():
                _handle.set_linestyle("--")
                _handle.set_dashes([2, 2])

    sim_fig.suptitle("biophysical model (simulated)", fontsize=16, fontweight="bold", x=0.61, y=1.03)

    sim_fig
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
