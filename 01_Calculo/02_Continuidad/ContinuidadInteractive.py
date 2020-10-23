{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.6"
    },
    "colab": {
      "name": "02_Continuidad_interactive.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "bc7effe878b44f97911e7207158ffe92": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "VBoxModel",
          "state": {
            "_view_name": "VBoxView",
            "_dom_classes": [
              "widget-interact"
            ],
            "_model_name": "VBoxModel",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "box_style": "",
            "layout": "IPY_MODEL_d966ea0c70d244aeb3da1bc25321bbba",
            "_model_module": "@jupyter-widgets/controls",
            "children": [
              "IPY_MODEL_e0987365b6074363817cbcab1f14d633",
              "IPY_MODEL_d8debd77dffa4400b7dafd54b9604e71",
              "IPY_MODEL_76b601bdb4074bc180dd15851bfd1b30"
            ]
          }
        },
        "d966ea0c70d244aeb3da1bc25321bbba": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "e0987365b6074363817cbcab1f14d633": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatSliderModel",
          "state": {
            "_view_name": "FloatSliderView",
            "style": "IPY_MODEL_895b0e2fd7ce4803855426416f356022",
            "_dom_classes": [],
            "description": "x0",
            "step": 0.5,
            "_model_name": "FloatSliderModel",
            "orientation": "horizontal",
            "max": 4.5,
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": 3.5,
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "min": 0.5,
            "continuous_update": true,
            "readout_format": ".2f",
            "description_tooltip": null,
            "readout": true,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_731a624a13464307a544f2fce5b0bae4"
          }
        },
        "d8debd77dffa4400b7dafd54b9604e71": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatSliderModel",
          "state": {
            "_view_name": "FloatSliderView",
            "style": "IPY_MODEL_de4443b28de4473d9a7fcf0ebb5bc292",
            "_dom_classes": [],
            "description": "delta",
            "step": 0.01,
            "_model_name": "FloatSliderModel",
            "orientation": "horizontal",
            "max": 0.5,
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": 0.05,
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "min": 0.01,
            "continuous_update": true,
            "readout_format": ".2f",
            "description_tooltip": null,
            "readout": true,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_09b345164acb41d7a50b7cd9ecc35e90"
          }
        },
        "76b601bdb4074bc180dd15851bfd1b30": {
          "model_module": "@jupyter-widgets/output",
          "model_name": "OutputModel",
          "state": {
            "_view_name": "OutputView",
            "msg_id": "",
            "_dom_classes": [],
            "_model_name": "OutputModel",
            "outputs": [
              {
                "output_type": "display_data",
                "metadata": {
                  "tags": [],
                  "needs_background": "light"
                },
                "image/png": "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\n",
                "text/plain": "<Figure size 720x360 with 1 Axes>"
              }
            ],
            "_view_module": "@jupyter-widgets/output",
            "_model_module_version": "1.0.0",
            "_view_count": null,
            "_view_module_version": "1.0.0",
            "layout": "IPY_MODEL_0d7ecec43f0f459db7d416887fa4e978",
            "_model_module": "@jupyter-widgets/output"
          }
        },
        "895b0e2fd7ce4803855426416f356022": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "state": {
            "_view_name": "StyleView",
            "handle_color": null,
            "_model_name": "SliderStyleModel",
            "description_width": "",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "731a624a13464307a544f2fce5b0bae4": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "de4443b28de4473d9a7fcf0ebb5bc292": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "state": {
            "_view_name": "StyleView",
            "handle_color": null,
            "_model_name": "SliderStyleModel",
            "description_width": "",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "09b345164acb41d7a50b7cd9ecc35e90": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "0d7ecec43f0f459db7d416887fa4e978": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        }
      }
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jugernaut/Prometeo/blob/desarrollo/01_Calculo/02_Continuidad/ContinuidadInteractive.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nQjdO5a8OHzZ",
        "outputId": "90545e0e-ddcf-4c8d-99c3-c953cd528a33",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        }
      },
      "source": [
        "!git clone https://github.com/joiortega1/Prueba_lectura.git\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import Prueba_lectura.gutils as vis\n",
        "%matplotlib inline\n",
        "from ipywidgets import interact, interactive, fixed\n",
        "import ipywidgets as widgets\n",
        "\n",
        "def continuidad(x, x0, delta, f):\n",
        "    y = f(x)                   # Codominio\n",
        "    y0 = f(x0)\n",
        "    x1 = x0 + delta\n",
        "    y1 = f(x1)\n",
        "    epsilon = np.fabs(y0 - y1)\n",
        "\n",
        "    par = [{'title':'$\\epsilon$ = {}, $\\delta$ = {}'.format(epsilon, delta), \n",
        "            'xlabel':'x',\n",
        "            'ylabel':'y'}]\n",
        "\n",
        "    graf = vis.planoCartesiano(par=par)\n",
        "    graf.plot(x=x, y=y, par={'label':'$f(x)=10\\cos(2x) + x^2$'})\n",
        "    graf.scatter(x=x0, y=y0, par={'color':'black', 'zorder':5})\n",
        "    graf.scatter(x=x1, y=y1, par={'color':'green', 'zorder':5})\n",
        "\n",
        "# Líneas verticales y horizontales\n",
        "    graf.plot(x = [x0, x0], y=[0, y0], par={'ls':'-', 'lw':2, 'color':'black'})\n",
        "    graf.plot(x = [0, x0], y=[y0, y0], par={'ls':'-', 'lw':2, 'color':'black'})\n",
        "    graf.plot(x = [x1, x1], y=[0, y1], par={'ls':'--', 'lw':2, 'color':'green'})\n",
        "    graf.plot(x = [0, x1], y=[y1, y1], par={'ls':'--', 'lw':2, 'color':'green'})\n",
        "\n",
        "    graf.plot(x = [x0, x1], y=[0, 0], par={'ls':'--', 'lw':1, 'color':'red'})\n",
        "    graf.plot(x = [0, 0], y=[y0, y1], par={'ls':'--', 'lw':1, 'color':'blue'})\n",
        "\n",
        "    offset1 = (y1-y0)*0.5\n",
        "    graf.annotate(par={'s':'$\\epsilon$', 'xy':(0, y0+offset1), 'xytext':(0.5,y0*1.2), \n",
        "                       'xycoords':'data','textcoords':'data', 'fontsize':15, 'color':'blue',\n",
        "                       'arrowprops':{'arrowstyle':'->', 'connectionstyle':'arc3', 'color':'blue'}\n",
        "                      })\n",
        "\n",
        "    offset2 = (x1-x0)*0.5\n",
        "    graf.annotate(par={'s':'$\\delta$', 'xy':(x0+offset2, 0), 'xytext':(x0*1.2,0.2), \n",
        "                       'xycoords':'data','textcoords':'data', 'fontsize':15, 'color':'red',\n",
        "                       'arrowprops':{'arrowstyle':'->', 'connectionstyle':'arc3', 'color':'red'}\n",
        "                      })\n",
        "    graf.legend(par={'loc':'lower right'})\n",
        "    graf.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'Prueba_lectura'...\n",
            "remote: Enumerating objects: 21, done.\u001b[K\n",
            "remote: Counting objects: 100% (21/21), done.\u001b[K\n",
            "remote: Compressing objects: 100% (17/17), done.\u001b[K\n",
            "remote: Total 21 (delta 1), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (21/21), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U9dUcfsWOH0V",
        "outputId": "6ed0161b-2342-4f37-d5aa-85c459c5460f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 462,
          "referenced_widgets": [
            "bc7effe878b44f97911e7207158ffe92",
            "d966ea0c70d244aeb3da1bc25321bbba",
            "e0987365b6074363817cbcab1f14d633",
            "d8debd77dffa4400b7dafd54b9604e71",
            "76b601bdb4074bc180dd15851bfd1b30",
            "895b0e2fd7ce4803855426416f356022",
            "731a624a13464307a544f2fce5b0bae4",
            "de4443b28de4473d9a7fcf0ebb5bc292",
            "09b345164acb41d7a50b7cd9ecc35e90",
            "0d7ecec43f0f459db7d416887fa4e978"
          ]
        }
      },
      "source": [
        "f = lambda x: 10*np.cos(2*x) + x**2\n",
        "x = np.linspace(0,5,100) \n",
        "w = interact(continuidad,\n",
        "             x = fixed(x),\n",
        "             x0 = widgets.FloatSlider(min=0.5, max=4.5, step=0.5, value=2.5),\n",
        "             delta= widgets.FloatSlider(min=0.01, max=.5, step=0.01, value=0.5),\n",
        "             f = fixed(f))\n",
        "display(w)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "bc7effe878b44f97911e7207158ffe92",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "interactive(children=(FloatSlider(value=2.5, description='x0', max=4.5, min=0.5, step=0.5), FloatSlider(value=…"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<function __main__.continuidad>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    }
  ]
}