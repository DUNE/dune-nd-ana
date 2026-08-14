from ndlar_caf_display.helpers import load_interaction_spills, plot_interactions
import argparse
import matplotlib

def main():
  parser = argparse.ArgumentParser(description="Display interactions from a CAF file.")
  parser.add_argument("caf_file", type=str, help="Path to the CAF file to display.")

  parser.add_argument("--spill", type=int, default=0, 
                      help="Spill number to display (default: 0th spill).")
  parser.add_argument("--ixn", type=int, default=None, nargs="+",
                      help="Interaction number(s) within the spill to display (default: 0th interaction).")
  parser.add_argument("--reco", type=str, default="dlp", choices=["dlp", "pandora"],
                      help="Reconstruction type to display: 'dlp' (spine) or 'pandora' (default: 'dlp').")
  parser.add_argument("--save-dir", type=str, default='plots', 
                      help="Directory to save plots (default: 'plots').")
  parser.add_argument("--skip-truth", action="store_true", default=False,
                      help="Whether to skip plotting truth information (default: False).")
  parser.add_argument("--apply-fv-cut", action="store_true", default=False,
                      help="Whether to apply the fiducial volume cut (default: False).")
  parser.add_argument("--batch", "-b", action="store_true", default=False,
                      help="Whether to run in batch mode where the plots are not displayed interactively (default: False).")
  parser.add_argument("--only-primary-reco", action="store_true", default=False,
                      help="Whether to plot only reconstructed primary particles (default: False).")
  parser.add_argument("--reco-energy-threshold", type=float, default=0.0,
                      help="Energy threshold for plotting reconstructed particles (default: 0.0 GeV).")

  args = parser.parse_args()

  if args.batch:
    matplotlib.use('Agg')  # Use a non-interactive backend for batch mode

  # Load interaction spills from the specified CAF file
  interaction_spills = load_interaction_spills(args.caf_file, reco=args.reco)

  kwargs = {
    "spill_index": args.spill,
    "reco": args.reco,
    "save_dir": args.save_dir,
    "plot_truth": not args.skip_truth,
    "apply_fv_cut": args.apply_fv_cut,
    "plot_only_primary_reco": args.only_primary_reco,
    "reco_energy_threshold": args.reco_energy_threshold
  }

  # Plot the interactions
  if args.ixn and len(args.ixn) == 1:
    kwargs["ixn"] = args.ixn[0]
    kwargs["mode"] = "single"
  elif args.ixn and len(args.ixn) > 1:
    kwargs["ixn_list"] = args.ixn
    kwargs["mode"] = "list"
  else:
    kwargs["mode"] = "all"
    
  plot_interactions(interaction_spills, **kwargs)

if __name__ == "__main__":
  main()